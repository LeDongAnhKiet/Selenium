# import json
class Bai3:
    def TuDien(self):
        dic = {
            'A': 'a',
            'B': 'b',
            'C': 'c'
        }
        dic.update({'Z': 'z'})
        print(dic)
        print('So luong: ', len(dic))
        n = 0
        key = 'Z'
        for k in dic.keys():
            if k == key:
                break
            else:
                n += 1
        if n == len(dic):
            print('Ko co')
        else:
            n = dic[k]
            del dic[k]
            print('Da xoa ', n)


# def load_data():
#     with open('data/dict.json', encoding='utf-8') as f:
#         return json.load(f)
#
#
# def save_data(data):
#     with open('data/dict.json', mode='w', encoding='utf-8') as f:
#         return json.dump(data, f, ensure_ascii=False, indent=4)
#
#
# def output_data(data):
#     if type(data) == dict:
#         for k, v in data.items():
#             print(f'{k} --> {v}')
#
#
# def add_word(data, word, meaning):
#     if word not in data:
#         data[word] = meaning
#         save_data(data)
#
#
# def delete_word(data, word):
#     if word in data:
#         del data[word]
#
#
# def find_word(data, word):
#     if word in data:
#         return data[word]
#
#

if __name__ == '__main__':
    a = Bai3()
    a.TuDien()
#     data = load_data()
#
#     add_word(data, "computer", "máy tính")
#     output_data(data)
#     print("====")
#     delete_word(data, "table")
#     output_data(data)
#     print(find_word(data, 'good'))
