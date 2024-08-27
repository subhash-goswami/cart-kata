from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import calculate_total
from .exceptions import InvalidItemError, PricingRuleError
from .pricing import PRICING_RULES


class CheckoutAPIView(APIView):

    def post(self, *args, **kwargs):
        try:
            items = self.request.data.get("items", "")
            total = calculate_total(items=items, pricing_rules=PRICING_RULES)
            return Response({"total": total}, status=status.HTTP_200_OK)

        except InvalidItemError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except PricingRuleError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
