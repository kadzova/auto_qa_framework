from pages.elements_page import TextBoxPage, CheckBoxPage
import time

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'the full name is not match'
            assert email == output_email, 'the email is not match'
            assert current_address == output_cur_address, 'the current address is not match'
            assert permanent_address == output_per_address, 'the permanent address is not match'

            # simplify the test but not informative

            # input_data = text_box_page.fill_all_fields
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            time.sleep(10)
            input_checkbox = check_box_page.get_checked_boxes()
            time.sleep(10)
            output_result = check_box_page.get_output_result()
            time.sleep(10)
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result

