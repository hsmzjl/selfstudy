// url编码解码
// 1、escape() 和 unescape()
// 原理：对除ASCII字母、数字、标点符号 @  *  _  +  -  .  / 以外的其他字符进行编码。

// 2、encodeURI() 和 decodeURI()
// 原理：返回编码为有效的统一资源标识符 (URI) 的字符串，不会被编码的字符：! @ # $ & * ( ) = : / ; ? + '
// 　　   encodeURI()是Javascript中真正用来对URL编码的函数。
// 编码：encodeURI(encodeURI(data.oneTypeName))
// 解码：decodeURI(request["OneTypeName"]);

// 3、encodeURIComponent() 和 decodeURIComponent()
// 原理：对URL的组成部分进行个别编码，而不用于对整个URL进行编码
// encodeURI(encodeURI(data.oneTypeName))
// decodeURI(request["OneTypeName"]);
