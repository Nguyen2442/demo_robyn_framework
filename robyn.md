worker event cycle 
Khi một trang web chạy JavaScript, các tác vụ được thực hiện trong một môi trường đơn luồng, nghĩa là chỉ có một luồng thực thi JavaScript trong trình duyệt. Tuy nhiên, để giải quyết vấn đề này, các trình duyệt đã triển khai một mô hình đa luồng với các "Worker" (nhân viên) để chạy các tác vụ trong nhiều luồng cùng một lúc.
Vòng đời sự kiện của worker (Worker event cycle) liên quan đến cách các tác vụ được xử lý trong một worker bao gồm việc đưa các tác vụ vào hàng đợi, xử lý chúng, và trả lại kết quả. Các sự kiện được xử lý trong một chu kỳ (cycle) và được quản lý bởi trình quản lý sự kiện của worker. 
-> Việc xử lý các sự kiện trong chu kỳ này giúp đảm bảo rằng các tác vụ trong worker được xử lý theo thứ tự và không bị xung đột với nhau.



Incoming requests
là các yêu cầu được gửi đến một máy chủ từ các thiết bị hoặc ứng dụng khác trên mạng hoặc internet. Các yêu cầu này thường được gửi từ các máy tính, trình duyệt web, thiết bị di động hoặc các ứng dụng khác sử dụng các giao thức như HTTP, FTP, SMTP, và SSH để tương tác với máy chủ.

Các incoming requests có thể bao gồm các yêu cầu như yêu cầu truy cập một trang web, yêu cầu tải xuống một tài liệu, yêu cầu thực hiện một tác vụ cụ thể, và các yêu cầu khác liên quan đến việc truy cập hoặc tương tác với các dịch vụ và tài nguyên trên mạng hoặc internet. Khi máy chủ nhận được các incoming requests, nó sẽ xử lý các yêu cầu này và trả lại kết quả tương ứng cho thiết bị hoặc ứng dụng đã gửi yêu cầu.


Rust runtime 

mã được biên dịch thành mã máy trực tiếp và chạy trên môi trường thực thi của hệ điều hành. 
Rust không có một thư viện tiêu chuẩn cho một runtime như các ngôn ngữ lập trình khác như Java hay Python. Tuy nhiên, Rust có thể được sử dụng để phát triển các ứng dụng web thông qua các framework như Rocket và actix-web, và các ứng dụng desktop thông qua framework như GTK và Qt.

Do Rust không có một runtime chuẩn, nên các lập trình viên thường phải tự xây dựng môi trường thực thi cho ứng dụng của họ, bao gồm việc xử lý các tác vụ như quản lý bộ nhớ, xử lý tác vụ bất đồng bộ, và phát triển các ứng dụng phân tán. Tuy nhiên, Rust có nhiều thư viện và công cụ hỗ trợ cho việc phát triển các ứng dụng phức tạp và an toàn.

Multithreaded Rust runtime
Runtime của Rust hỗ trợ việc thực thi đồng thời nhiều luồng để tăng hiệu suất


Rust object

Mỗi đối tượng trong Rust được định nghĩa bởi một struct hoặc enum, và các thuộc tính của đối tượng được định nghĩa bởi các trường (fields) trong struct hoặc các variant trong enum.



Trong Tokio, một worker là một task (hoặc coroutine) được chạy trên một thread của hệ thống. Tokio sử dụng một thread pool để quản lý các worker, đảm bảo rằng có đủ các worker để xử lý các tác vụ đến, và tối ưu hóa việc sử dụng tài nguyên hệ thống.

Mỗi worker chịu trách nhiệm xử lý một hoặc nhiều tác vụ (tasks) cùng một lúc. Khi một task mới được đưa vào hệ thống, nó được đưa vào một trong những worker có sẵn. Nếu tất cả các worker đang bận, thì một worker mới sẽ được tạo ra để xử lý task mới.

Các worker trong Tokio được xử lý bởi một event loop (vòng lặp sự kiện) đảm bảo rằng các tasks được thực thi theo cách không đồng bộ và hiệu quả. Khi một task yêu cầu một hoạt động đồng bộ như đọc hoặc ghi dữ liệu, worker sẽ "không đóng băng" (không chặn) và chuyển task này sang một worker khác. Điều này cho phép các worker khác có thể thực hiện các tác vụ khác trong khi task đang chờ kết quả trả về, giúp tối ưu hóa thời gian xử lý và tăng hiệu suất của hệ thống.


Event loop (vòng lặp sự kiện) là một kỹ thuật lập trình đa luồng phổ biến được sử dụng trong các hệ thống đa luồng hoặc đa nhiệm. Nó được sử dụng để quản lý và xử lý các sự kiện (events) trong hệ thống. Một event loop có thể được hiểu như một vòng lặp vô hạn, nó lặp đi lặp lại để kiểm tra và xử lý các sự kiện mới khi chúng xảy ra. Khi một sự kiện xảy ra, event loop sẽ thực hiện một số tác vụ xử lý nhất định được chỉ định cho sự kiện đó. Sau đó, nó quay trở lại chế độ chờ đợi để chờ đợi các sự kiện mới.

Event loop được sử dụng rộng rãi trong các ứng dụng mạng để xử lý các kết nối mạng và các sự kiện IO (nhập/xuất). Các thư viện và framework như asyncio (Python), Tokio (Rust), Node.js (JavaScript) và libevent (C) đều sử dụng event loop để cung cấp các tính năng bất đồng bộ và đa luồng trong các ứng dụng mạng.


Trong Tokio, một process (quá trình) được hiểu là một tác vụ có thể thực thi độc lập với các tác vụ khác, tương tự như một luồng (thread) trong các hệ thống đa luồng. Tuy nhiên, một tiến trình thường có chi phí cấu hình và duy trì cao hơn một luồng, do đó thường được sử dụng cho các tác vụ cần thực thi trên một quy mô lớn hoặc có tính chất bất đồng bộ (asynchronous).

Các quá trình trong Tokio được triển khai bằng cách sử dụng tokio::task::spawn_blocking để chạy các tác vụ đồng bộ. Khi một tác vụ được đưa vào một quá trình, Tokio sẽ tự động tạo ra một luồng riêng để thực thi tác vụ đó, trong khi vẫn giữ cho event loop chính đang chạy và xử lý các tác vụ bất đồng bộ khác. Tuy nhiên, việc sử dụng quá trình cũng cần được cân nhắc để tránh tình trạng đồng thời quá nhiều quá trình chạy đồng thời, gây ra tốn tài nguyên và hiệu suất ứng dụng giảm sút.




Const Requests
là một tính năng của robyn
thực thi function chỉ một lần và lưu response trong rust response 


Trong Robyn, Arc<RouteMap> là một smart pointer trong Rust, nó đại diện cho một vùng nhớ được cấp phát động được chia sẻ giữa nhiều chủ thể mà không cần sao chép dữ liệu.

RouteMap là một cấu trúc dữ liệu để lưu trữ các route được đăng ký trong Robyn. Bằng cách sử dụng Arc<RouteMap>, chúng ta có thể truy cập và thao tác với các route được lưu trữ trong RouteMap mà không cần phải quan tâm đến việc chia sẻ vùng nhớ giữa các chủ thể và các vấn đề liên quan đến bộ thu gom rác.

Trong ConstRouter, Arc<RouteMap> được sử dụng để lưu trữ các route được đăng ký và để truy cập các route này khi có yêu cầu từ các yêu cầu của người dùng.


Output struct trong Robyn sử dụng bộ nhớ heap để lưu trữ response. Cụ thể, trường value trong struct được khai báo kiểu Arc<Vec<u8>>, với Arc là một smart pointer để quản lý vùng nhớ heap, và Vec<u8> là một vector chứa các byte của response. Do đó, khi tạo một instance của Output, vùng nhớ cho value sẽ được cấp phát trên heap và được giải phóng khi không còn được sử dụng.


Trong Robyn, const request được sử dụng để định nghĩa các tài nguyên tĩnh được phục vụ cho ứng dụng. Tài nguyên tĩnh bao gồm các tệp tĩnh như HTML, CSS, JavaScript, hình ảnh, v.v.

Khi một yêu cầu HTTP được nhận từ phía client, nó sẽ được so khớp với các route được đăng ký và nếu không có route phù hợp, Robyn sẽ kiểm tra xem có tài nguyên tĩnh tương ứng với đường dẫn yêu cầu không. Nếu có, nó sẽ trả về tài nguyên tĩnh đó.

Với const request, Robyn cung cấp cho bạn một cách dễ dàng để phục vụ các tài nguyên tĩnh trong ứng dụng của bạn, giúp bạn tập trung vào việc xây dựng các tính năng quan trọng hơn cho ứng dụng của mình.


************
Nếu sử dụng const request cho các routing không cố định, có nghĩa là chúng ta chỉ cho phép xử lý một số request cố định trước, không cho phép xử lý các request có động dinh, ví dụ như request với query parameters khác nhau. Điều này có thể làm hạn chế tính linh hoạt của ứng dụng, nếu ứng dụng của bạn có nhiều routing động. Trong trường hợp này, nên sử dụng các Router khác như MatchItRouter hoặc RegexRouter của Robyn, để cho phép các routing động và linh hoạt hơn.



--workers là một tùy chọn khi chạy ứng dụng bằng lệnh dòng lệnh để xác định số lượng worker process sẽ được sử dụng để xử lý các yêu cầu của client.

Mỗi worker process là một phiên bản của ứng dụng được chạy đồng thời, giúp tăng khả năng chịu tải của ứng dụng bằng cách xử lý nhiều yêu cầu đồng thời. Tuy nhiên, tăng số lượng worker process cũng đồng nghĩa với việc tăng tài nguyên hệ thống sử dụng và cần phải cân nhắc để tránh tình trạng quá tải hệ thống.

Với mỗi worker process được sử dụng, Robyn sẽ sử dụng một thread pool để xử lý các yêu cầu của client. Số lượng thread trong thread pool được xác định bởi --max-threads option trong cấu hình Robyn.

Worker trong Tokio Runtime là một loại thực thể được sử dụng để thực thi các Future. Mỗi worker được quản lý bởi một thread riêng biệt, có nhiệm vụ chạy và quản lý các Future được gửi đến nó.

Khi một Future được gửi đến worker, nó được thực thi và worker tiếp tục chạy các Future khác trên cùng một thread. Khi một Future được hoàn thành hoặc gặp phải một lỗi, kết quả được trả về cho caller, và worker sẽ tiếp tục chạy các Future khác trên cùng một thread.

Một trong những điểm mạnh của Tokio Runtime là khả năng quản lý động các worker để đáp ứng với các yêu cầu tải khác nhau. Điều này có nghĩa là, khi một ứng dụng được triển khai trong một môi trường có tải lớn, Tokio Runtime có thể tự động tăng số lượng worker để đáp ứng với nhu cầu xử lý của ứng dụng. Nó cũng có thể giảm số lượng worker khi tải giảm đi, để tiết kiệm tài nguyên và giảm độ trễ của hệ thống.



Trong Robyn, --processes là tùy chọn để thiết lập số lượng worker process (quá trình xử lý) được tạo ra để xử lý các yêu cầu (requests) đến từ client. Mỗi worker process được tạo ra để xử lý các yêu cầu và trả về các kết quả tương ứng. Thiết lập số lượng worker process có thể giúp tăng tốc độ xử lý yêu cầu của ứng dụng.

Ví dụ: Nếu bạn thiết lập --processes 4 thì sẽ có 4 worker process được tạo ra để xử lý các yêu cầu từ client.


Trong Robyn, một worker là một quá trình (process) đang chạy chương trình, mỗi worker đều có thể xử lý nhiều yêu cầu (request) đồng thời bằng cách sử dụng coroutine để đồng bộ các tác vụ. Mỗi worker có thể chạy trên một CPU core hoặc một thread riêng.

Trong khi đó, một process là một chương trình đang chạy trên hệ thống. Mỗi process có một bộ nhớ độc lập, có thể chia sẻ dữ liệu giữa các process thông qua IPC (Inter-Process Communication). Khi bạn chạy Robyn với nhiều processes, nghĩa là bạn đang chạy nhiều phiên bản của ứng dụng Robyn song song trên các process khác nhau. Mỗi process chạy một instance của ứng dụng Robyn, và có thể xử lý nhiều yêu cầu của client đồng thời bằng cách sử dụng nhiều worker.

Tổng quan về quá trình hoạt động của Robyn khi có nhiều worker và process:

Mỗi worker được chạy trên một thread hoặc một core CPU.
Mỗi process là một bản sao độc lập của ứng dụng Robyn, chạy trên một bộ nhớ độc lập và có thể chia sẻ dữ liệu thông qua IPC.
Mỗi yêu cầu của client sẽ được chuyển đến một worker bất kỳ trong process đang chạy.
Nếu một process bị treo hoặc bị tắt, các yêu cầu của client sẽ được chuyển đến các process khác.