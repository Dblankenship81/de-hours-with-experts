from secret_recipe_decoder import decode_ingredient, decode_string, Ingredient

def test_decode_string_can_decode():
    assert(decode_string("yhv") == "abc")

def test_decode_ingredient_can_decode():
    expected = Ingredient("1 cup", "butter")
    actual = decode_ingredient("8 vgl#hgiikf")
    assert(actual.amount == expected.amount)
    assert(actual.description == expected.description)