# Result:
## 实验过程
我们使用不同的编码方式对"original_expression.txt"文件进行压缩、解压操作。这里我们约定编码过程中8个比特位为一个码字。

对于LZW过程中字典长度超过规定的比特位数为重新刷新字典，反之为不刷新字典；对于LZ系列的算法最后生成的字典的key值，在实际过程中key值是连续递增的，将最后的结果按固定比特位数进行存为二进制文件为定长生成文件；

首先我们使用哈夫曼编码的方式对该文件进行压缩。

再者我们采取的方式是LZW加上不刷新字典的方式，初始化字典为0-255，进过压缩后产生的结果的码字长度最大的是15，采取用定长来生产二进制文件，最后的结果会比原有文件要大。这是由于在压缩过程中字典没有进行重新生成，且通过LZW算法可以知道最后结果中每个码字的重复率极低，所以用最长的15位表示压缩后的码字会造成压缩后结果变长。为了降低压缩后码字的长度，我们采用不定长编码的方式，即对压缩后结果经过哈夫曼编码。并且测试了刷新字典下的压缩情况。

最后我们使用LZ77算法进行编码，将滑动窗口分别设为8、32、128、256（单位是码字），并对结果进行哈夫曼编码，我们可以发现压缩结果越来越小，但是随着滑动窗口的增加，计算的复杂度也随之增大。


## 实验结果与分析
通过实验结果我们可以知道定长表示会使得压缩的结果变大，对于LZW算法重新生产字典可以避免压缩结果增加，对于LZ77算法，压缩结果有明显下降趋势，但是滑动窗口过大会造成计算的困难，通过分析LZ77算法，我们可以发现，造成算法的复杂在于匹配最长字符串，由于本次实验中采取的是暴力匹配的方式，所以当华东窗口超过256后计算会很复杂。



# 结论
本实验的做到的最好的压缩率为93.8%，文件大约30kb，并未压缩到老师要求的30kb以下。LZW属于LZ78的一种，LZ78和LZ77都是基于字典的无损压缩算法，在实际应用中有许多应用。

根据实验过程中存在的一些问题对进一步的工作提出一些优化的设想：
- 由于LZ77增大滑动窗口，压缩率减少的特点，可以通过优化LZ77算法中最长字符串匹配，使得可以使用更大的滑动窗口来压缩文件；
- 对于LZW算法，可以在压缩过程中计算压缩率，在压缩率下降到一定长度才清除字典；或者不清楚全部字典，更具使用情况来清楚部分字典；
- 混合使用LZ77和LZW。在发现标记匹配结束后，不立即结束匹配，而是在一个滑动窗口中寻找是否有更好的匹配，如果有，就将位置和匹配长度写入输出流中，并把该字符串逐个增加为标记。

