from ...utils import get_graphql_content

CHECKOUT_ADD_PROMO_CODE_MUTATION = """
mutation AddCheckoutPromoCode($checkoutId: ID!, $promoCode: String!) {
  checkoutAddPromoCode(id: $checkoutId, promoCode: $promoCode) {
    checkout {
      id
      discount{
        amount
      }
      discountName
      lines{
        totalPrice{
          gross{
            amount
          }
        }
        undiscountedTotalPrice{
          amount
        }
        unitPrice{
          gross{
            amount
          }
        }
        undiscountedUnitPrice{
          amount
        }
      }
    }
    errors {
      code
      field
      message
    }
  }
}
"""


def checkout_add_promo_code(
    staff_api_client,
    checkout_id,
    code,
):
    variables = {
        "checkoutId": checkout_id,
        "promoCode": code,
    }

    response = staff_api_client.post_graphql(
        CHECKOUT_ADD_PROMO_CODE_MUTATION, variables
    )
    content = get_graphql_content(response)

    assert content["data"]["checkoutAddPromoCode"]["errors"] == []

    return content["data"]["checkoutAddPromoCode"]["checkout"]