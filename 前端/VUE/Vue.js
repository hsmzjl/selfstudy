// 引入
<body>
	<div id="app">
		{{ message }} {{ name }}
		<p>{{ job }}</p>
		<a v-bind:href='website'>web开发</a>
		<input type="text" v-bind:value="job"></input>  //绑定属性    
		<p v-html='webtag'></p>    //绑定html
		<button v-on:click='add'>加一</button>   //绑定单击事件    v-on:  可以用@来替代
		<p v-html='webtag'>My age is {{age}}</p>
		<button v-on:mousemove='move'>加一</button>  //绑定鼠标移动事件
		<input type="text" v-model="thename"></input>  //双向数据绑定
		<span>{{thename}}</span>
		</div>

	<script type="text/javascript">
		var app = new Vue({
			el: '#app',
		data: {
			message: 'Hello Vue!',
			name : "Vue",
			job:'ddddd',
			website:'www.baidu.com',
			webtag:"<a href='website'>这是一个a标签</a>",
			age:10,
			thename:""
		},
		methods:{
			greet:function() {
				return 'Hello'+this.name;    //直接使用data数据
			},
			add:function () {
				return age++
			}
			move:function (event) {     //鼠标事件会自动传入事件参数
				console.log(event)
			}
		}
	});
	</script>
	
	el:VUE需要绑定的元素
	data:用于数据的储存
	mathods:用于储存各种方法
	data-binging:给属性绑定特定的值













</body>