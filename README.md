# IR_evaluation
1、简介：本代码实现不同的信息检索指标的计算，主要包含 p@5、p@10、p@20、recall@5、recall@10、recall@15、f1、AP、NGDC@5、NGDC@10、NGDC@20等指标。
2、代码框架：采用python flask。 
3、接口介绍：
（1）接口url：http://127.0.0.1:5000/evaluation/
（2）输入：
a.参数1：数据类型：列表；值：标准数据集的doc_id列表
b.参数2：数据类型：列表；值：检索结果的doc_id列表
（3）输出：各个评价指标的值
（4）数据传输格式：采用json数据格式进行传输
