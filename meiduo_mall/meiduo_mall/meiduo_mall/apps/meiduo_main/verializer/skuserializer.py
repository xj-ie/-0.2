from django.db import transaction
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from goods.models import SKU

from goods.models import GoodsVisitCount

from goods.models import GoodsCategory

from goods.models import SPUSpecification

from goods.models import SpecificationOption


class SkuSerializer(ModelSerializer):

    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

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
                    SPUSpecification.objects.create(specs_id = spec["specs_id"],option_id=spec["option_id"],sku=sku)
            except Exception as e:
                transaction.savepoint_rollback(save_point)
                raise serializers.ValidationError(e)


        return sku


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