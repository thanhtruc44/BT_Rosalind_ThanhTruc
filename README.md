# BT_Rosalind_ThanhTruc
# Bài tập về Kmer, Consensus và Assemble
## Bài tập 1: Đếm k-mer lặp lại trong Chuỗi DNA
### Mô tả
Chương trình Python này đếm số lần xuất hiện của k-mer (chuỗi con có độ dài k) xuất hiện hơn hai lần trong một chuỗi DNA được cung cấp với giá trị k tối thiểu là 10. Nó lấy một tệp FASTA chứa chuỗi DNA làm đầu vào và đưa ra các k-mer lặp lại cùng với số lần xuất hiện. Chương trình mang lại nhiều ý nghĩa sinh học và ứng dụng to lớn: phân tích tổ hợp gen; phát hiện và phân loại chuỗi ứng dụng trong phân loại các loại gen và loại vi khuẩn; tìm kiếm motif; dự đoán khả năng liên kết với protein; phân tích genome và nhiều ứng dụng đang nghiên cứu
### Yêu cầu
- Python 3.x
- Thư viện argparse
### Sử dụng
1. Cài đặt thư viện Python cần thiết:
pip install argparse
2. Chạy chương trình bằng câu lệnh sau:
python script.py tên_tệp [--k K]
- `tên_tệp` là đường dẫn đến tệp FASTA chứa chuỗi DNA.
- `--k K` chỉ định độ dài tối thiểu của k-mer. Giá trị mặc định là 10.
3. Chương trình sẽ xuất ra các k-mer lặp lại và số lần xuất hiện của chúng.
### Ví dụ
python script.py sequence.fasta --k 10
### Giấy phép
Dự án này được cấp phép theo [Giấy phép MIT].
### Liên hệ
Để biết thêm thông tin hoặc có ý kiến đóng góp, vui lòng liên hệ qua trucle2k2@gmail.com.
