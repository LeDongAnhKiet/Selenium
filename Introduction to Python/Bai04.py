# import json
class Bai4:
    employees = [{
        "ma_nv": 1,
        "ten_nv": "Nguyễn Văn A",
    }, {
        "ma_nv": 2,
        "ten_nv": "Dương Trọng C",
    }, {
        "ma_nv": 3,
        "ten_nv": "Nguyễn Thanh N",
    }]
    # def load_data():
    #     with open('data/emp.json', encoding='utf-8') as f:
    #         return json.load(f)
    #
    #
    # def save_data(data):
    #     with open('data/emp.json', mode='w', encoding='utf-8') as f:
    #         return json.dump(data, f, ensure_ascii=False, indent=4)
    #
    #
    # def output(data):
    #     for em in data:
    #         for k, v in em.items():
    #             if k == 'ma_nv':
    #                 print(f'Mã nhân viên: {v}')
    #             elif k == 'ten_nv':
    #                 print(f'Tên nhân viên: {v}')
    #
    #
    # def add_emp(data, ma_nv, ten_nv):
    #     e = {
    #         "ma_nv": ma_nv,
    #         "ten_nv": ten_nv
    #     }
    #     data.append(e)
    #     save_data(data)
    #
    #
    # def delete_emp(data, ma_nv):
    #     for idx, em in enumerate(data):
    #         if em['ma_nv'] == ma_nv:
    #             del data[idx]
    #             save_data(data)
    #             break
    #     else:
    #         print('Không có nhân viên này.')
    #
    #
    # def find_emp(data, kw):
    #     for em in data:
    #         if em['ten_nv'].find(kw) >= 0:
    #             print(em['ma_nv'])
    #
    #
# if __name__ == '__main__':
#     data = load_data()
#     output(data)
#     #add_emp(data, 9, 'Trần Thị B')
#     delete_emp(data, 3)
#     find_emp(data, 'Văn')
