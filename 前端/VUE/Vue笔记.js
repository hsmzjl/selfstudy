Vue.component('button-counter', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
  })

new Vue({
    el:"#app",
    data:{
        a:"888"
    }
})


//--------------------------------------- 插值---------------------------------------------

// 文本
// 数据绑定最常见的形式就是使用“Mustache”语法 (双大括号) 的文本插值：
<span>Message: {{ msg }}</span>
// Mustache 标签将会被替代为对应数据对象上 msg property 的值。无论何时，绑定的数据对象上 msg property 发生了改变，插值处的内容都会更新。
// 通过使用 v-once 指令，你也能执行一次性地插值，当数据改变时，插值处的内容不会更新。但请留心这会影响到该节点上的其它数据绑定：
<span v-once>这个将不会改变: {{ msg }}</span>

// 原始 HTML
// 双大括号会将数据解释为普通文本，而非 HTML 代码。为了输出真正的 HTML，你需要使用 v-html 指令：
<p>Using mustaches: {{ rawHtml }}</p>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>
// 这个 span 的内容将会被替换成为 property 值 rawHtml，直接作为 HTML——会忽略解析 property 值中的数据绑定。
// 注意，你不能使用 v-html 来复合局部模板，因为 Vue 不是基于字符串的模板引擎。反之，对于用户界面 (UI)，组件更适合作为可重用和可组合的基本单位。
// 你的站点上动态渲染的任意 HTML 可能会非常危险，因为它很容易导致 XSS 攻击。请只对可信内容使用 HTML 插值，绝不要对用户提供的内容使用插值。

// Attribute 属性绑定
// Mustache 语法不能作用在 HTML attribute 上，遇到这种情况应该使用 v-bind 指令：
<div v-bind:id="dynamicId"></div>
// 对于布尔 attribute (它们只要存在就意味着值为 true)，v-bind 工作起来略有不同，在这个例子中：
<button v-bind:disabled="isButtonDisabled">Button</button>
// 如果 isButtonDisabled 的值是 null、undefined 或 false，则 disabled attribute 甚至不会被包含在渲染出来的 <button> 元素中。

// 使用 JavaScript 表达式
// 迄今为止，在我们的模板中，我们一直都只绑定简单的 property 键值。但实际上，对于所有的数据绑定，Vue.js 都提供了完全的 JavaScript 表达式支持。
{{ number + 1 }}
{{ ok ? 'YES' : 'NO' }}
{{ message.split('').reverse().join('') }}
<div v-bind:id="'list-' + id"></div>
// 这些表达式会在所属 Vue 实例的数据作用域下作为 JavaScript 被解析。有个限制就是，每个绑定都只能包含单个表达式，所以下面的例子都不会生效。
// <!-- 这是语句，不是表达式 -->
{{ var a = 1 }}
// <!-- 流控制也不会生效，请使用三元表达式 -->
{{ if (ok) { return message } }}
// 模板表达式都被放在沙盒中，只能访问全局变量的一个白名单，如 Math 和 Date 。你不应该在模板表达式中试图访问用户定义的全局变量。


// --------------------------------------------指令--------------------------------------------
// 指令 (Directives) 是带有 v- 前缀的特殊 attribute。
// 指令 attribute 的值预期是单个 JavaScript 表达式 (v-for 是例外情况，稍后我们再讨论)。
// 指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。回顾我们在介绍中看到的例子：
<p v-if="seen">现在你看到我了</p>
// 这里，v-if 指令将根据表达式 seen 的值的真假来插入/移除 <p> 元素。

// 参数
// 一些指令能够接收一个“参数”，在指令名称之后以冒号表示。例如，v-bind 指令可以用于响应式地更新 HTML attribute：
<a v-bind:href="url">...</a>
// 在这里 href 是参数，告知 v-bind 指令将该元素的 href attribute 与表达式 url 的值绑定。
// 另一个例子是 v-on 指令，它用于监听 DOM 事件：
<a v-on:click="doSomething">...</a>
// 在这里参数是监听的事件名。我们也会更详细地讨论事件处理。

// 动态参数
// 从 2.6.0 开始，可以用方括号括起来的 JavaScript 表达式作为一个指令的参数：
// <!--
// 注意，参数表达式的写法存在一些约束，如之后的“对动态参数表达式的约束”章节所述。
// -->
<a v-bind:[attributeName]="url"> ... </a>
// 这里的 attributeName 会被作为一个 JavaScript 表达式进行动态求值，求得的值将会作为最终的参数来使用。
// 例如，如果你的 Vue 实例有一个 data property attributeName，其值为 "href"，那么这个绑定将等价于 v-bind:href。
// 同样地，你可以使用动态参数为一个动态的事件名绑定处理函数：
<a v-on:[eventName]="doSomething"> ... </a>
// 在这个示例中，当 eventName 的值为 "focus" 时，v-on:[eventName] 将等价于 v-on:focus。
// 对动态参数的值的约束
// 动态参数预期会求出一个字符串，异常情况下值为 null。这个特殊的 null 值可以被显性地用于移除绑定。任何其它非字符串类型的值都将会触发一个警告。
// 对动态参数表达式的约束
// 动态参数表达式有一些语法约束，因为某些字符，如空格和引号，放在 HTML attribute 名里是无效的。例如：
// <!-- 这会触发一个编译警告 -->
<a v-bind:['foo' + bar]="value"> ... </a>
// 变通的办法是使用没有空格或引号的表达式，或用计算属性替代这种复杂表达式。
// 在 DOM 中使用模板时 (直接在一个 HTML 文件里撰写模板)，还需要避免使用大写字符来命名键名，因为浏览器会把 attribute 名全部强制转为小写：
// <!--
// 在 DOM 中使用模板时这段代码会被转换为 `v-bind:[someattr]`。
// 除非在实例中有一个名为“someattr”的 property，否则代码不会工作。
// -->
<a v-bind:[someAttr]="value"> ... </a>

// 修饰符
// 修饰符 (modifier) 是以半角句号 . 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。例如，.prevent 修饰符告诉 v-on 指令对于触发的事件调用 event.preventDefault()：
<form v-on:submit.prevent="onSubmit">...</form>
// 在接下来对 v-on 和 v-for 等功能的探索中，你会看到修饰符的其它例子。


// --------------------------------------------------缩写----------------------------------------
// v- 前缀作为一种视觉提示，用来识别模板中 Vue 特定的 attribute。当你在使用 Vue.js 为现有标签添加动态行为 (dynamic behavior) 时，v- 前缀很有帮助，
// 然而，对于一些频繁用到的指令来说，就会感到使用繁琐。同时，在构建由 Vue 管理所有模板的单页面应用程序 (SPA - single page application) 时，
// v- 前缀也变得没那么重要了。因此，Vue 为 v-bind 和 v-on 这两个最常用的指令，提供了特定简写：

// v-bind 缩写
// <!-- 完整语法 -->
<a v-bind:href="url">...</a>
// <!-- 缩写 -->
<a :href="url">...</a>
// <!-- 动态参数的缩写 (2.6.0+) -->
<a :[key]="url"> ... </a>

// v-on 缩写
// <!-- 完整语法 -->
<a v-on:click="doSomething">...</a>
// <!-- 缩写 -->
<a @click="doSomething">...</a>
// <!-- 动态参数的缩写 (2.6.0+) -->
<a @[event]="doSomething"> ... </a>
// 它们看起来可能与普通的 HTML 略有不同，但 : 与 @ 对于 attribute 名来说都是合法字符，在所有支持 Vue 的浏览器都能被正确地解析。
// 而且，它们不会出现在最终渲染的标记中。缩写语法是完全可选的，但随着你更深入地了解它们的作用，你会庆幸拥有它们。


// -------------------------------------------计算属性和侦听器-----------------------------------------

// 计算属性
// 模板内的表达式非常便利，但是设计它们的初衷是用于简单运算的。在模板中放入太多的逻辑会让模板过重且难以维护。例如：

<div id="example">
  {{ message.split('').reverse().join('') }}
</div>
// 在这个地方，模板不再是简单的声明式逻辑。你必须看一段时间才能意识到，这里是想要显示变量 message 的翻转字符串。当你想要在模板中多包含此处的翻转字符串时，就会更加难以处理。
// 所以，对于任何复杂逻辑，你都应当使用计算属性。

// 基础例子
<div id="example">
  <p>Original message: "{{ message }}"</p>
  <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
})
// 结果：
Original message: "Hello"
Computed reversed message: "olleH"

// 这里我们声明了一个计算属性 reversedMessage。我们提供的函数将用作 property vm.reversedMessage 的 getter 函数：
console.log(vm.reversedMessage) // => 'olleH'
vm.message = 'Goodbye'
console.log(vm.reversedMessage) // => 'eybdooG'
// 你可以打开浏览器的控制台，自行修改例子中的 vm。vm.reversedMessage 的值始终取决于 vm.message 的值。
// 你可以像绑定普通 property 一样在模板中绑定计算属性。
// Vue 知道 vm.reversedMessage 依赖于 vm.message，因此当 vm.message 发生改变时，所有依赖 vm.reversedMessage 的绑定也会更新。
// 而且最妙的是我们已经以声明的方式创建了这种依赖关系：计算属性的 getter 函数是没有副作用 (side effect) 的，这使它更易于测试和理解。



// 计算属性缓存 vs 方法
// 你可能已经注意到我们可以通过在表达式中调用方法来达到同样的效果：
<p>Reversed message: "{{ reversedMessage() }}"</p>
// 在组件中
methods: {
  reversedMessage: function () {
    return this.message.split('').reverse().join('')
  }
}
// 我们可以将同一函数定义为一个方法而不是一个计算属性。两种方式的最终结果确实是完全相同的。然而，不同的是计算属性是基于它们的响应式依赖进行缓存的。
// 只在相关响应式依赖发生改变时它们才会重新求值。这就意味着只要 message 还没有发生改变，多次访问 reversedMessage 计算属性会立即返回之前的计算结果，而不必再次执行函数。
// 这也同样意味着下面的计算属性将不再更新，因为 Date.now() 不是响应式依赖：

computed: {
  now: function () {
    return Date.now()
  }
}
// 相比之下，每当触发重新渲染时，调用方法将总会再次执行函数。
// 我们为什么需要缓存？假设我们有一个性能开销比较大的计算属性 A，它需要遍历一个巨大的数组并做大量的计算。然后我们可能有其他的计算属性依赖于 A。
// 如果没有缓存，我们将不可避免的多次执行 A 的 getter！如果你不希望有缓存，请用方法来替代。



// 计算属性 vs 侦听属性
// Vue 提供了一种更通用的方式来观察和响应 Vue 实例上的数据变动：侦听属性。
// 当你有一些数据需要随着其它数据变动而变动时，你很容易滥用 watch——特别是如果你之前使用过 AngularJS。然而，通常更好的做法是使用计算属性而不是命令式的 watch 回调。
// 细想一下这个例子：
<div id="demo">{{ fullName }}</div>
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar',
    fullName: 'Foo Bar'
  },
  watch: {
    firstName: function (val) {
      this.fullName = val + ' ' + this.lastName
    },
    lastName: function (val) {
      this.fullName = this.firstName + ' ' + val
    }
  }
})
// 上面代码是命令式且重复的。将它与计算属性的版本进行比较：

var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar'
  },
  computed: {
    fullName: function () {
      return this.firstName + ' ' + this.lastName
    }
  }
})
// 好得多了，不是吗？


// 计算属性的 setter
// 计算属性默认只有 getter，不过在需要时你也可以提供一个 setter：
// ...
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
// ...
// 现在再运行 vm.fullName = 'John Doe' 时，setter 会被调用，vm.firstName 和 vm.lastName 也会相应地被更新。


// 侦听器
// 虽然计算属性在大多数情况下更合适，但有时也需要一个自定义的侦听器。
// 这就是为什么 Vue 通过 watch 选项提供了一个更通用的方法，来响应数据的变化。当需要在数据变化时执行异步或开销较大的操作时，这个方式是最有用的。
// 例如：
<div id="watch-example">
  <p>
    Ask a yes/no question:
    <input v-model="question">
  </p>
  <p>{{ answer }}</p>
</div>
{/* <!-- 因为 AJAX 库和通用工具的生态已经相当丰富，Vue 核心代码没有重复 --> */}
{/* <!-- 提供这些功能以保持精简。这也可以让你自由选择自己更熟悉的工具。 --> */}
<script src="https://cdn.jsdelivr.net/npm/axios@0.12.0/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lodash@4.13.1/lodash.min.js"></script>
<script>
var watchExampleVM = new Vue({
  el: '#watch-example',
  data: {
    question: '',
    answer: 'I cannot give you an answer until you ask a question!'
  },
  watch: {
    // 如果 `question` 发生改变，这个函数就会运行
    question: function (newQuestion, oldQuestion) {
      this.answer = 'Waiting for you to stop typing...'
      this.debouncedGetAnswer()
    }
  },
  created: function () {
    // `_.debounce` 是一个通过 Lodash 限制操作频率的函数。
    // 在这个例子中，我们希望限制访问 yesno.wtf/api 的频率
    // AJAX 请求直到用户输入完毕才会发出。想要了解更多关于
    // `_.debounce` 函数 (及其近亲 `_.throttle`) 的知识，
    // 请参考：https://lodash.com/docs#debounce
    this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
  },
  methods: {
    getAnswer: function () {
      if (this.question.indexOf('?') === -1) {
        this.answer = 'Questions usually contain a question mark. ;-)'
        return
      }
      this.answer = 'Thinking...'
      var vm = this
      axios.get('https://yesno.wtf/api')
        .then(function (response) {
          vm.answer = _.capitalize(response.data.answer)
        })
        .catch(function (error) {
          vm.answer = 'Error! Could not reach the API. ' + error
        })
    }
  }
})
</script>
{/* 结果： */}
Ask a yes/no question:  
I cannot give you an answer until you ask a question!
{/* 在这个示例中，使用 watch 选项允许我们执行异步操作 (访问一个 API)，限制我们执行该操作的频率，并在我们得到最终结果前，设置中间状态。
这些都是计算属性无法做到的。除了 watch 选项之外，您还可以使用命令式的 vm.$watch API。 */}




{/* -------------------------------------------------Class 与 Style 绑定---------------------------------------------------------- */}

{/* 操作元素的 class 列表和内联样式是数据绑定的一个常见需求。因为它们都是 attribute，所以我们可以用 v-bind 处理它们：只需要通过表达式计算出字符串结果即可。
不过，字符串拼接麻烦且易错。因此，在将 v-bind 用于 class 和 style 时，Vue.js 做了专门的增强。表达式结果的类型除了字符串之外，还可以是对象或数组。 */}

{/* 绑定 HTML Class */}

{/* 对象语法
我们可以传给 v-bind:class 一个对象，以动态地切换 class： */}
<div v-bind:class="{ active: isActive }"></div>
{/* 上面的语法表示 active 这个 class 存在与否将取决于数据 property isActive 的 truthiness。
你可以在对象中传入更多字段来动态切换多个 class。此外，v-bind:class 指令也可以与普通的 class attribute 共存。当有如下模板： */}
<div 
  class="static"
  v-bind:class="{ active: isActive, 'text-danger': hasError }"
></div>
{/* 和如下 data： */}
data: {
  isActive: true,
  hasError: false
}
{/* 结果渲染为： */}
<div class="static active"></div>
{/* 当 isActive 或者 hasError 变化时，class 列表将相应地更新。例如，如果 hasError 的值为 true，class 列表将变为 "static active text-danger"。
绑定的数据对象不必内联定义在模板里： */}
<div v-bind:class="classObject"></div>
data: {
  classObject: {
    active: true,
    'text-danger': false
  }
}
{/* 渲染的结果和上面一样。我们也可以在这里绑定一个返回对象的计算属性。这是一个常用且强大的模式： */}
<div v-bind:class="classObject"></div>
data: {
  isActive: true,
  error: null
},
computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}

{/* 数组语法
我们可以把一个数组传给 v-bind:class，以应用一个 class 列表： */}
<div v-bind:class="[activeClass, errorClass]"></div>
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}

{/* 渲染为： */}
<div class="active text-danger"></div>
{/* 如果你也想根据条件切换列表中的 class，可以用三元表达式： */}
<div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>
{/* 这样写将始终添加 errorClass，但是只有在 isActive 是 truthy[1] 时才添加 activeClass。 */}
{/* 不过，当有多个条件 class 时这样写有些繁琐。所以在数组语法中也可以使用对象语法： */}
<div v-bind:class="[{ active: isActive }, errorClass]"></div>

{/* 用在组件上
这个章节假设你已经对 Vue 组件有一定的了解。当然你也可以先跳过这里，稍后再回过头来看。
当在一个自定义组件上使用 class property 时，这些 class 将被添加到该组件的根元素上面。这个元素上已经存在的 class 不会被覆盖。
例如，如果你声明了这个组件： */}
Vue.component('my-component', {
  template: '<p class="foo bar">Hi</p>'
})
{/* 然后在使用它的时候添加一些 class： */}
<my-component class="baz boo"></my-component>
{/* HTML 将被渲染为： */}
<p class="foo bar baz boo">Hi</p>
{/* 对于带数据绑定 class 也同样适用： */}
<my-component v-bind:class="{ active: isActive }"></my-component>
{/* 当 isActive 为 truthy[1] 时，HTML 将被渲染成为： */}
<p class="foo bar active">Hi</p>
{/* 绑定内联样式
对象语法
v-bind:style 的对象语法十分直观——看着非常像 CSS，但其实是一个 JavaScript 对象。CSS property 名可以用驼峰式 (camelCase) 或短横线分隔 (kebab-case，记得用引号括起来) 来命名： */}
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
data: {
  activeColor: 'red',
  fontSize: 30
}
{/* 直接绑定到一个样式对象通常更好，这会让模板更清晰： */}
<div v-bind:style="styleObject"></div>
data: {
  styleObject: {
    color: 'red',
    fontSize: '13px'
  }
}
{/* 同样的，对象语法常常结合返回对象的计算属性使用。 */}

{/* 数组语法
v-bind:style 的数组语法可以将多个样式对象应用到同一个元素上： */}
<div v-bind:style="[baseStyles, overridingStyles]"></div>
{/* 自动添加前缀
当 v-bind:style 使用需要添加浏览器引擎前缀的 CSS property 时，如 transform，Vue.js 会自动侦测并添加相应的前缀。 */}

{/* 多重值
2.3.0+
从 2.3.0 起你可以为 style 绑定中的 property 提供一个包含多个值的数组，常用于提供多个带前缀的值，例如： */}

<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
// 这样写只会渲染数组中最后一个被浏览器支持的值。在本例中，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 display: flex。





























