a = 'tracnghiem.txt'
b = 'tracnghiem_ketqua.txt'
c = [1, 2, 3, 4]
d = [1, 2, 3]
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def tao_file_tracnghiem():
  noi_dung = '''1. Người mạnh mẽ có đặc điểm gì? 1-Tay to, 2-Tay nhỏ, 3-Chân dài, 4-Chân Ngắn:
2. Người khéo léo có đặc điểm gì? 1-Tay to, 2-Tay nhỏ, 3-Chân dài, 4-Chân Ngắn:
3. Người nhanh nhẹn có đặc điểm gì? 1-Tay to, 2-Tay nhỏ, 3-Chân dài, 4-Chân Ngắn:
4. Người kiên trì có đặc điểm gì? 1-Tay to, 2-Tay nhỏ, 3-Chân dài, 4-Chân Ngắn:'''

  with open(a, 'w', encoding='utf-8') as f:
    f.write(noi_dung)


def doc_file_trac_nghiem(filename):
  with open(filename, 'r', encoding='utf-8') as f:
    g = f.readlines()
  return g


def hien_thi_cau_hoi(i):
  j = []
  for k, l in enumerate(i):
    print(l.strip())
    m = int(input(f"Câu trả lời của bạn (1-4): "))
    j.append(m)
  return j


def kiem_tra_ket_qua(o, p):
  q = []
  for r in range(len(o)):
    if o[r] == p[r]:
      q.append(f"Câu {r+1}: Đúng")
    else:
      q.append(f"Câu {r+1}: Sai")
  return q


def luu_ket_qua(t, u):
  with open(t, 'w', encoding='utf-8') as f:
    for v in u:
      f.write(v + '\n')


if __name__ == "__main__":
  tao_file_tracnghiem()
  cau_hoi = doc_file_trac_nghiem(a)
  cau_tra_loi = hien_thi_cau_hoi(cau_hoi)
  ket_qua = kiem_tra_ket_qua(cau_tra_loi, c)
  luu_ket_qua(b, ket_qua)
  print(f"Kết quả đã được lưu vào {b}")
