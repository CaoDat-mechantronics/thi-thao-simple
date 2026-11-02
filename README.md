# THẢO THÚ CƯNG – WEBSITE NHIỀU TRANG

## Khởi động
Giải nén và mở `index.html` bằng Chrome/Edge/Firefox. Website không yêu cầu cài đặt, không dùng CDN, hoạt động offline.

## Cấu trúc
- `index.html`: trang chủ giống banner mẫu + 6 danh mục + khu hot + khu khuyến mãi + sản phẩm theo danh mục.
- `danh-muc-cho.html`, `danh-muc-meo.html`, `danh-muc-suc-khoe.html`, `danh-muc-dinh-duong.html`, `danh-muc-phu-kien.html`, `danh-muc-bo-sung.html`: 6 trang danh mục riêng.
- `san-pham-hot.html`: trang tổng hợp sản phẩm nổi bật.
- `khuyen-mai.html`: trang tổng hợp sản phẩm có giá demo giảm.
- `tat-ca-san-pham.html`: trang toàn bộ 24 sản phẩm, tìm kiếm và sắp xếp.
- `chi-tiet-<id>.html`: 24 trang HTML chi tiết từng sản phẩm, ví dụ `chi-tiet-cho-01.html`.
- `catalog.js`: dữ liệu tên, giá, mô tả, ảnh của 24 sản phẩm. Chỉnh tại đây khi thay hàng hóa.
- `site.js`: hiển thị danh sách/trang chi tiết, giỏ hàng localStorage và nút tương tác.
- `site.css`: giao diện responsive theo phong cách ảnh tham chiếu.
- `assets/`: hình gốc + 24 hình sản phẩm minh họa. Giữ nguyên thư mục khi upload.

## Chức năng hiện có
- Liên kết giữa trang chủ, 6 danh mục, 2 trang hot/khuyến mãi, 24 trang chi tiết.
- Tìm kiếm sản phẩm qua tên, mô tả, danh mục; sắp xếp giá/tên.
- Thêm sản phẩm vào giỏ, điều chỉnh số lượng, xóa sản phẩm. Giỏ được lưu trong localStorage (trên cùng origin).
- Trang chi tiết có ảnh, mô tả, số lượng, sản phẩm cùng danh mục.
- Menu responsive, nút yêu thích, pop-up giỏ hàng.

## Quan trọng
Website là giao diện demo. Sản phẩm, bao bì, giá gốc, giá ưu đãi, chính sách và thông tin liên hệ đều minh họa. Không có thanh toán, xử lý đơn, xác thực tài khoản hay backend. Khi đưa vào kinh doanh cần cập nhật sản phẩm và liên hệ thật, xây dựng backend và xác minh nội dung.

Nếu chạy bằng file://, mỗi trình duyệt có thể giới hạn lưu trữ localStorage. Khi deploy lên GitHub Pages / hosting tĩnh, giỏ hàng sẽ dùng cùng origin trên các trang.


## Đồng bộ giao diện và font chữ (bản cập nhật)
- **Tất cả 35 trang HTML** dùng chung thanh điều hướng và một font chữ.
- Font chính: `Nunito`, độ đậm menu **900/1000**, bo tròn gần giống ảnh tham chiếu. Dùng Google Fonts khi có mạng; nếu offline thì tự động chuyển sang `Arial Rounded MT Bold` / `Trebuchet MS`.
- Biểu tượng trang chủ, sản phẩm, khuyến mãi, hàng hot, giới thiệu, tìm kiếm, tài khoản và giỏ hàng dùng SVG nét viền thay vì ký tự/emoji có kiểu khác nhau giữa các máy.
- Mục đang mở được làm nổi bật bằng nền cam, chữ trắng. Menu trên desktop trang chủ nằm trong ảnh banner gốc (để giữ hình ban đầu giống mẫu); các trang còn lại và trang chủ trên điện thoại dùng menu HTML chung.
- Chỉnh lại kích thước và bo góc chữ ở `site.css`, phần `ĐỒNG BỘ CHỮ / HEADER THEO ẢNH MẪU`.


## Cập nhật liên kết mạng xã hội và ảnh chụp thật (02-11-2026)
- Nút Facebook (trong banner và chân trang của mọi trang) dẫn đến https://www.facebook.com/.
- Nút TikTok dẫn đến https://www.tiktok.com/@dattotbung?_r=1&_t=ZS-9Aw6fqmqA7w (giữ đủ tham số).
- Nút Zalo dẫn đến https://zalo.me/; nút điện thoại chưa có số nên vẫn ở chế độ demo.
- 11/24 sản phẩm tham chiếu ảnh chụp thực tế từ Wikimedia Commons. Ảnh là ảnh minh họa thể loại sản phẩm chứ KHÔNG đại diện chính xác cho nhãn hiệu, thành phần hay SKU. Ảnh tải từ Internet, nếu không có Internet hoặc nguồn bị chặn, website tự hiển thị hình minh họa cũ (vẫn nằm trong ZIP).
- Trang `nguon-anh.html` ghi đầy đủ nguồn, tác giả, giấy phép. Các trang chi tiết có liên kết đến nguồn ảnh.
- Cấu trúc HTML, menu, danh mục, giỏ hàng, màu sắc và banner trang chủ được giữ nguyên.

### Tải ảnh thật về để website hoạt động cả khi offline (tùy chọn)
Website ban đầu sử dụng ảnh thật qua đường dẫn trực tuyến của Wikimedia Commons (không đóng gói sẵn file ảnh chụp trong ZIP). Nếu muốn tải chúng về máy để dùng offline:
1. Cài Python và thư viện Pillow (`pip install Pillow`) nếu chưa có.
2. Trên Windows, mở `tai_anh_that.bat`; hoặc chạy `python download_real_photos.py`.
3. Chương trình lưu ảnh tại `assets/real-photos/` và cập nhật `catalog.js` để dùng ảnh offline cho những file tải thành công.
Nguồn và giấy phép vẫn được ghi trong `nguon-anh.html`.
