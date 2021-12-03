import allure


class Check:
    @staticmethod
    @allure.step
    def equality(obj1, obj2, is_equal=True):
        if is_equal:
            assert obj1 == obj2
        else:
            assert obj1 != obj2
