from rest_framework import serializers

from .models import DoneByEnum, Item, ItemStatusEnum, ItemTypeEnum


class ItemSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=ItemStatusEnum.choices(), required=False)
    type = serializers.ChoiceField(choices=ItemTypeEnum.choices())
    done_by = serializers.ChoiceField(
        choices=[("", "")] + DoneByEnum.choices(), allow_blank=True, required=False
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "date",
            "done_by",
            "task",
            "type",
            "status",
            "quantity",
            "base_gvt",
            "gvt_earned",
        ]

    def validate(self, data):
        quantity = data.get("quantity")
        base_gvt = data.get("base_gvt")
        gvt_earned = data.get("gvt_earned")
        if quantity is not None and base_gvt is not None and gvt_earned is not None:
            expected = float(quantity) * float(base_gvt)
            # Accept small rounding errors
            if abs(float(gvt_earned) - expected) > 0.01:
                raise serializers.ValidationError(
                    {"gvt_earned": "GVT Earned must be equal to Quantity × Base GVT."}
                )
        return data
