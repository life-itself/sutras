(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{230:function(t,e,r){var content=r(233);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,r(51).default)("77022c2a",content,!0,{sourceMap:!1})},232:function(t,e,r){"use strict";r(230)},233:function(t,e,r){var n=r(50)((function(i){return i[1]}));n.push([t.i,'body{\n  font-family:Inter,Raleway,sans-serif\n}\nh1,h2,h3,h4{\n  font-family:"Libre Baskerville",serif\n}\n.footnote-ref,div.footnotes{\n  font-size:small\n}',""]),t.exports=n},248:function(t,e,r){"use strict";r.r(e);var n=r(6),c=(r(38),{asyncData:function(t){return Object(n.a)(regeneratorRuntime.mark((function e(){var r,n,article;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=t.$content,n=t.params,e.next=3,r("sutras",n.slug).fetch();case 3:return article=e.sent,e.abrupt("return",{article:article});case 5:case"end":return e.stop()}}),e)})))()}}),o=(r(232),r(48)),component=Object(o.a)(c,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("article",{staticClass:"prose lg:prose-xl max-w-2xl mx-auto pt-36"},[r("h1",[t._v(t._s(t.article.title))]),t._v(" "),r("p",{staticClass:"text-sm"},[t._v("\n    Source: "),r("a",{attrs:{href:t.article.source}},[t._v(" "+t._s(t.article.source))]),t._v(" "),r("br"),r("br"),t._v("\n    Alternative sources: "),r("a",{attrs:{href:t.article.alt}},[t._v(" "+t._s(t.article.alt))])]),t._v(" "),r("nuxt-content",{attrs:{document:t.article}})],1)}),[],!1,null,null,null);e.default=component.exports}}]);