

class TestCalc:

    def test_add(self,get_calc,get_add_datas):
        result = get_calc.add(get_add_datas[0],get_add_datas[1])
        assert result == get_add_datas[2]

    def test_sub(self, get_calc,get_sub_datas):
        result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        assert result == get_sub_datas[2]

    def test_mul(self,get_calc,get_mul_datas):
        result = get_calc.mul(get_mul_datas[0],get_mul_datas[1])
        assert result == get_mul_datas[2]

    def test_div(self, get_calc,get_div_datas):
        result = get_calc.div(get_div_datas[0], get_div_datas[1])
        assert result == get_div_datas[2]
