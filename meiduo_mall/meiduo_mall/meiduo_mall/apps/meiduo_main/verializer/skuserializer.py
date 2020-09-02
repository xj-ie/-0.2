from django.db import transaction
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from goods.models import SKU, SKUSpecification

from goods.models import GoodsVisitCount

from goods.models import GoodsCategory

from goods.models import SPUSpecification

from goods.models import SpecificationOption

class SKUSpecificationSserializer(ModelSerializer):
    # options =  SpecificationOptionSerializer(many=True)
    # specificationoption_set = SpecificationOptionSerializer(many=True)
    spec_id = serializers.IntegerField(read_only=True)
    option_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = SKUSpecification
        fields = ('spec_id',"option_id")

class SkuSerializer(ModelSerializer):

    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    specs = SKUSpecificationSserializer(read_only=True,many=True)
    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'
        read_only_fields = ("spu","category")

    def create(self, validated_data):
        specs = self.context["request"].data.get("specs")
        with transaction.atomic():
            save_point = transaction.savepoint()
            try:
                sku = SKU.objects.create(**validated_data)
                for spec in specs:
                    SKUSpecification.objects.create(spec_id = spec["spec_id"],option_id=spec["option_id"],sku=sku)
            except Exception as e:
                transaction.savepoint_rollback(save_point)
                raise serializers.ValidationError(e)

            else:
                transaction.savepoint_commit(save_point)
                return sku
    def update(self, instance, validated_data):
        specs = self.context["request"].data.get("specs")
        with transaction.atomic():
            save_point = transaction.savepoint()
            try:
                sku = SKU.objects.filter(id=instance.id).update(**validated_data)
                for spec in specs:
                    SKUSpecification.objects.filter(sku=sku).update(**spec)
            except Exception as e:
                transaction.savepoint_rollback(save_point)

                raise serializers.ValidationError(e)
            finally: return instance

class GoodsVisitSerializer(ModelSerializer):
    class Meta:
        model = GoodsCategory

        fields = "__all__"


class SpecificationOptionSerializer(ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = '__all__'
class SPUSpecificationSerializer(ModelSerializer):

    options =  SpecificationOptionSerializer(many=True)
    # specificationoption_set = SpecificationOptionSerializer(many=True)
    class Meta:
        model = SPUSpecification
        fields = '__all__'