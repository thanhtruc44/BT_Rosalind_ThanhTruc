# BT_Rosalind_ThanhTruc
# Bài tập về Kmer, Consensus và Assemble
## Bài tập 1: Đếm các k-mer lặp lại trong chuỗi DNA
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
### Tác giả
- Tên tác giả: Lê Thanh Trúc
- Năm sinh: 2002
### Liên hệ
Để biết thêm thông tin hoặc có ý kiến đóng góp, vui lòng liên hệ qua trucle2k2@gmail.com. 
### Giấy phép
Dự án này được cấp phép theo [MIT License].
## Bài tập 2: Xây dựng trình tự đồng thuận từ các chuỗi DNA có cùng kích thước
### Mô tả
Chương trình Python này tính toán trình tự đồng thuận (consensus string) dựa trên profile matrix của các nucleotide với dữ liệu đầu vào là một tệp FASTA chứa các chuỗi DNA dựa trên profile matrix của các nucleotide. Chương trình này có nhiều ứng dụng to lớn: Giảm sự sai lệch và nhiễu dữ liệu bằng cách kết hợp thông tin từ nhiều chuỗi và tạo ra một chuỗi "tổng hợp" chính xác hơn; xác định các biến thể và đa dạng bằng cách xác định các biến thể và đa dạng trong tập dữ liệu DNA hoặc protein; tạo ra genome reference giúp cung cấp một trình tự đại diện cho loài hoặc biến thể cụ thể và là một dữ liệu quan trọng trong nghiên cứu sinh học và y học; phân tích chức năng gen: xây dựng trình tự đồng thuận có thể hỗ trợ phân tích chức năng gen bằng cách tạo ra một trình tự đại diện cho gen hoặc các vùng quan trọng của gen
### Yêu cầu
- Python 3.x
- Thư viện Bio của Python: `pip install biopython`
### Cài đặt
1. Tải mã nguồn chương trình từ [GitHub] (https://github.com/thanhtruc44/BT_Rosalind_ThanhTruc.git)
2. Cài đặt các yêu cầu với pip: `pip install -r requirements.txt`
### Sử dụng
1. Đặt tệp FASTA chứa các chuỗi DNA cần tính toán vào cùng thư mục với chương trình và đổi tên tệp thành `Seq02.fasta` hoặc chỉnh sửa tên tệp trong mã nguồn chương trình.
2. Mở cửa sổ dòng lệnh và di chuyển đến thư mục chứa chương trình.
3. Chạy chương trình: `python your_program.py`
4. Kết quả sẽ được hiển thị trên cửa sổ dòng lệnh và ghi lại vào tệp `consensus.log`.
### Cấu trúc dự án
- `your_program.py`: Mã nguồn chương trình chính.
- `Seq02.fasta`: Tệp ví dụ chứa các chuỗi DNA.
- `consensus.log`: Tệp ghi lại quá trình chạy của chương trình.
### Tác giả
- Tên tác giả: Lê Thanh Trúc
- Năm sinh: 2002
### Liên hệ
Để biết thêm thông tin hoặc có ý kiến đóng góp, vui lòng liên hệ qua trucle2k2@gmail.com. 
### Giấy phép
Chương trình này được phân phối dưới giấy phép [MIT License]
