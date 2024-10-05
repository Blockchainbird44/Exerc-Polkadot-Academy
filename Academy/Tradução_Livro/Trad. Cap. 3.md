# Functional-Light JavaScript

# Capítulo 3: Entradas de Função

No capítulo 2, exploramos a natureza fundamental das funções em JS e lançamos as bases para o que torna uma função uma função FP. Mas, para aproveitar todo o poder do FP, também precisamos de padrões e práticas para manipular funções para mudar e ajustar suas interações - para 'dobrá-las' à nossa vontade.

Especificamente, nossa atenção neste capítulo será sobre os parâmetros de entrada das funções. À medida que você junta funções de todos os tipos diferentes em seus programas, você rapidamente enfrentará incompatibilidades no número/ordem/tipo de entradas, bem como a necessidade de especificar algumas entradas em momentos diferentes de outros.

Na verdade, para fins de estilo e legibilidade, às vezes você vai querer definir funções de uma forma que esconda suas entradas completamente!

Esses tipos de técnicas são absolutamente essenciais para tornar funções verdadeiramente funcionais.

## Todos por um

Imagine que você está passando uma função para uma utilidade, onde a utilidade enviará vários argumentos para essa função. Mas você pode querer que a função receba apenas um argumento.

Podemos projetar um auxiliar simples que envolve uma chamada de função para garantir que apenas um argumento passará. Como isso efetivamente impõe que uma função seja tratada como unária (função com somente uma variável), vamos chamá-la como tal:

<a name="unary"></a>

```js
function unary(fn) {
  return function onlyOneArg(arg) {
    return fn(arg);
  };
}
```

Muitos FPers tendem a preferir a sintaxe de função de seta `=>` mais curta para esse tipo de código (veja Capítulo 2, "Funções sem `function`"), como:

```js
var unary = (fn) => (arg) => fn(arg);
```

Nota: Não há dúvida de que isso é mais conciso, até mesmo esparso. Mas, pessoalmente, sinto que por mais que ganhe em simetria com a notação matemática, perde mais em legibilidade geral com todas as funções sendo anônimas, e ao obscurecer os limites do escopo, tornando a decifração do fechamento um pouco mais codificada.

Um exemplo comumente citado para a utilização de `unary(...)` é com o utilitário `map(...)` (veja Capítulo 9, "Map") e `parseInt(...)`. O `map(...)` chama uma função mapper para cada item de uma lista, e cada vez que ele invoca a função mapper, ele passa três argumentos: `value`, `idx`, `arr`.

Isso normalmente não é um grande problema, a não ser que esteja tentando utilizar algo como uma função de mapeamento que se comportará incorretamente se lhe forem passados demasiados argumentos. Considere:

```js
["1", "2", "3"].map(parseInt);
// [1,NaN,NaN]
```

Para a assinatura `parseInt(str,radix)`, é evidente que quando `map(...)` passa `index` na posição do segundo argumento, este é interpretado por `parseInt(...)` como o `radix`, o que não queremos.

`unary(...)` cria uma função que irá ignorar todos os argumentos passados, exceto o primeiro, o que significa que o `index` passado nunca é recebido por `parseInt(...)` e confundido com o `radix`:

<a name="mapunary"></a>

```js
["1", "2", "3"].map(unary(parseInt));
// [1,2,3]
```

### Um para um

Por falar em funções com apenas um argumento, outro utilitário de base comum no conjunto de ferramentas da FP é uma função que recebe um argumento e não faz nada para além de devolver o valor inalterado:

```js
function identity(v) {
  return v;
}

// or the ES6 => arrow form
var identity = (v) => v;
```

Este utilitário parece tão simples que dificilmente será útil. Mas, mesmo as funções simples podem ser úteis no mundo do FP. Como se diz no teatro: não há papéis pequenos, apenas atores pequenos.

Por exemplo, imagine que você gostaria de dividir uma string usando uma expressão regular, mas o array resultante pode ter alguns valores vazios. Para descartá-los, podemos usar a operação de array `filter(...)` do JS (veja Capítulo 9, "Filter") com `identity(...)` como predicado:

```js
var words = "   Now is the time for all...  ".split(/\s|\b/);
words;
// ["","Now","is","the","time","for","all","...",""]

words.filter(identity);
// ["Now","is","the","time","for","all","..."]
```

Porque `identity(..)` simplesmente retorna o valor passado para ela, o JS converte cada valor em `true` ou `false`, e isso determina se o valor será mantido ou excluído do array final.

**Dica:** Outra função unária que pode ser usada como exemplificado no exemplo anterior é a função `Boolean(..)` do JS, que converte explicitamente um valor para `true` ou `false`.

Outro exemplo de uso de `identity(..)` é como uma função padrão no lugar de uma transformação:

```js
function output(msg, formatFn = identity) {
  msg = formatFn(msg);
  console.log(msg);
}

function upper(txt) {
  return txt.toUpperCase();
}

output("Hello World", upper); // HELLO WORLD
output("Hello World"); // Hello World
```

Você também pode ver `identity(..)` sendo usada como uma função de transformação padrão para chamadas de `map(..)` ou como o valor inicial em uma `reduce(..)` de uma lista de funções. Ambas as utilidades serão abordadas no Capítulo 9.

### O Imutável

Certas APIs não permitem que você passe um valor diretamente para um método, exigindo que você passe uma função, mesmo que essa função simplesmente retorne o valor. Uma dessas APIs é o método `then(..)` em Promises do JS:

```js
// como não funciona:
p1.then(foo).then(p2).then(bar);

// como funciona:
p1.then(foo)
  .then(function () {
    return p2;
  })
  .then(bar);
```

Muitos afirmam que as funções de seta ES6 `=>` são a melhor "solução":

```js
p1.then(foo)
  .then(() => p2)
  .then(bar);
```

Mas existe uma utilidade FP que é mais adequada para a tarefa:

```js
function constant(v) {
  return function value() {
    return v;
  };
}

// ou a forma de seta ES6 =>
var constant = (v) => () => v;
```

Com essa pequena e organizada funcionalidade FP, podemos resolver nossa irritação com `then(..)` adequadamente:

```js
p1.then(foo).then(constant(p2)).then(bar);
```

**Aviso:** Embora a versão da função tipo seta `() => p2` seja mais curta que `constant(p2)`, eu o encorajo a resistir à tentação de usá-la. A função de seta está retornando um valor de fora de si mesma, o que é um pouco pior da perspectiva da FP. Abordaremos as armadilhas de tais ações mais adiante no capítulo 5 do livro.

## Adaptando Argumentos a Parâmetros

Existem vários padrões e truques que podemos usar para adaptar a assinatura de uma função para corresponder aos tipos de argumentos que queremos fornecer a ela.

Lembre-se desta assinatura de função do Capítulo 2 que destaca o uso de desestruturação de parâmetros de array:

```js
function foo( [x,y,...args] = [] ) {
```

Este padrão é útil se um array for passado, mas somente se você quiser tratar seu conteúdo como parâmetros individuais. `foo(..)` é, portanto, tecnicamente unário - quando é executado, e apenas um argumento (um array) será passado a ele. Mas dentro da função, você pode endereçar diferentes entradas (`x`, `y`, etc) individualmente.

No entanto, às vezes você não terá a capacidade de alterar a declaração da função para usar a desestruturação de parâmetros de array. Por exemplo, imagine essas funções:

```js
function foo(x, y) {
  console.log(x + y);
}

function bar(fn) {
  fn([3, 9]);
}

bar(foo); // falhou
```

Você consegue identificar por que `bar(foo)` falha?

O array `[3,9]` é enviado como um único valor para `fn(..)`, mas `foo(..)` espera `x` e `y` separadamente. Se pudéssemos mudar a declaração de `foo(..)` para `function foo([x,y]) { ..`, estaríamos bem. Ou, se pudéssemos mudar o comportamento de `bar(..)` para fazer a chamada como `fn(...[3,9])`, os valores `3` e `9` seriam passados individualmente.

Haverá ocasiões em que você terá duas funções que são incompatíveis dessa forma e você não poderá mudar suas declarações/definições. Então, como você pode usá-las juntas?

Podemos definir um auxiliar para adaptar uma função para que ela espalhe um único array recebido como seus argumentos individuais:

<a name="spreadargs"></a>

```js
function spreadArgs(fn) {
  return function spreadFn(argsArr) {
    return fn(...argsArr);
  };
}

// ou a forma de seta ES6 =>
var spreadArgs = (fn) => (argsArr) => fn(...argsArr);
```

**Nota:** Eu chamei esse auxiliar `spreadArgs(..)`, mas em bibliotecas como Ramda ele é comumente chamado de `apply(..)`.

Agora podemos usar `spreadArgs(..)` para adaptar `foo(..)` para funcionar como a entrada correta para `bar(..)`:

```js
bar(spreadArgs(foo)); // 12
```

Ainda não parecerá claro por que essas ocasiões surgem, mas você as verá com frequência. Essencialmente, `spreadArgs(..)` nos permite definir funções que `retornam` vários valores por meio de um array, mas ainda têm esses vários valores tratados independentemente, como entradas para outra função.

Enquanto estamos falando sobre uma utilidade `spreadArgs(..)`, vamos também definir uma utilidade para lidar com a ação oposta:

```js
function gatherArgs(fn) {
  return function gatheredFn(...argsArr) {
    return fn(argsArr);
  };
}

// ou a forma de seta ES6 =>
var gatherArgs =
  (fn) =>
  (...argsArr) =>
    fn(argsArr);
```

**Nota:** Em Ramda, essa utilidade é referida como `unapply(..)`, isto é o oposto de `apply(..)`. Acho que a terminologia "spread"/"gather" é um pouco mais descritiva para o que está acontecendo.

Podemos usar essa utilidade para reunir argumentos individuais em um único array, talvez porque queiramos adaptar uma função com desestruturação de parâmetro de array para outra utilidade que passa argumentos separadamente. Abordaremos o `reduce(..)` mais completamente no Capítulo 9; resumidamente, ele chama repetidamente sua função redutora com dois parâmetros individuais, que agora podemos _gather_ (ou _reunir_) juntos:

```js
function combineFirstTwo([v1, v2]) {
  return v1 + v2;
}

[1, 2, 3, 4, 5].reduce(gatherArgs(combineFirstTwo)); // 15
```

## Alguns Agora, Outros Depois

Se uma função recebe múltiplos argumentos, você pode querer especificar alguns deles antecipadamente e deixar o resto para ser especificado depois.

Considere esta função:

```js
function ajax(url, data, callback) {
  // ..
}
```

Vamos imaginar que você gostaria de configurar várias chamadas de API em que as URLs são conhecidas antecipadamente, mas os dados e o retorno de chamada para lidar com a resposta não serão conhecidos até um momento posterior.

Claro, você pode simplesmente adiar a realização da chamada `ajax(..)` até que todos os bits sejam conhecidos e se referir a alguma constante global para a URL naquele momento. Mas outra maneira é criar uma referência de função que já tenha o argumento `url` predefinido.

O que vamos fazer é criar uma nova função que ainda chama `ajax(..)` nos bastidores, e ela define manualmente o primeiro argumento para a URL da API que você se importa, enquanto espera para aceitar os outros dois argumentos mais tarde:

```js
function getPerson(data, cb) {
  ajax("http://some.api/person", data, cb);
}

function getOrder(data, cb) {
  ajax("http://some.api/order", data, cb);
}
```

Especificar manualmente esses wrappers de chamada de função é certamente possível, mas pode se tornar bastante tedioso, especialmente se também houver variações com diferentes argumentos predefinidos, como:

```js
function getCurrentUser(cb) {
  getPerson({ user: CURRENT_USER_ID }, cb);
}
```

Uma prática que um (FPer) se acostuma muito é procurar padrões onde fazemos os mesmos tipos de coisas repetidamente e tentar transformar essas ações em utilitários genéricos reutilizáveis. Na verdade, tenho certeza de que esse já é o instinto de muitos de vocês, leitores, então isso não é exclusivamente uma coisa de FP. Mas é inquestionavelmente importante para FP.

Para conceber tal utilidade para a pré-configuração de argumentos, vamos examinar conceitualmente o que está acontecendo, não apenas olhando para as implementações manuais mostradas aqui.

Uma maneira de articular o que está acontecendo é que a função `getOrder(data,cb)` é uma _aplicação parcial_ da função `ajax(url,data,cb)`. Essa terminologia vem da noção de que os argumentos são _aplicados_ aos parâmetros no local da chamada da função. E, como você pode ver, estamos aplicando apenas alguns dos argumentos a priori - especificamente, o argumento para o parâmetro `url` - enquanto deixamos o resto para ser aplicado posteriormente.

Para ser um pouco mais formal sobre esse padrão, a aplicação parcial é estritamente uma redução na ariedade de uma função; lembre-se, esse é o número de entradas de parâmetros esperadas. Reduzimos a ariedade da função original `ajax(..)` de 3 para 2 para a função `getOrder(..)`.

Vamos definir uma utilidade `partial(..)`:

```js
function partial(fn, ...presetArgs) {
  return function partiallyApplied(...laterArgs) {
    return fn(...presetArgs, ...laterArgs);
  };
}

// ou a forma de seta ES6 =>
var partial =
  (fn, ...presetArgs) =>
  (...laterArgs) =>
    fn(...presetArgs, ...laterArgs);
```

**Dica:** Não apenas aceite este trecho no seu valor nominal. Pause por alguns momentos para digerir o que está acontecendo com essa utilidade. Certifique-se de realmente _entender_.

A função `partial(..)` recebe um `fn` para qual função estamos aplicando parcialmente. Então, quaisquer argumentos subsequentes passados são reunidos no array `presetArgs` e salvos para mais tarde.

Uma nova função interna (chamada `partiallyApplied(..)` apenas para facilitação) é criada e `retornada`; os argumentos da própria função interna são reunidos em um array chamado `laterArgs`.

Consegue observar as referências a `fn` e `presetArgs` dentro dessa função interna? Como isso funciona? Depois que `partial(..)` termina de executar, como a função interna continua sendo capaz de acessar `fn` e `presetArgs`? Se você respondeu **closure**, você está no caminho certo! A função interna `partiallyApplied(..)` fecha sobre as variáveis `fn` e `presetArgs` para que possa continuar acessando-as mais tarde, não importa onde a função seja executada. É por isso que entender o closure(fechamento) é crítico!

Quando a função `partiallyApplied(..)` é executada posteriormente em outro lugar do seu programa, ela usa o `fn` fechado para executar a função original, primeiro fornecendo quaisquer argumentos de aplicação parcial (fechados) `presetArgs`, então quaisquer outros argumentos `laterArgs`.

Se alguma coisa disso foi confusa, pare e leia novamente. Confie em mim, você ficará feliz por ter feito isso à medida que avançamos no texto.

Vamos agora usar a utilidade `partial(..)` para criar aquelas funções aplicadas parcialmente anteriores:

```js
var getPerson = partial(ajax, "http://some.api/person");

var getOrder = partial(ajax, "http://some.api/order");
```

Reserve um momento para considerar a forma/argumentos internos de `getPerson(..)`. Vai parecer mais ou menos assim:

```js
var getPerson = function partiallyApplied(...laterArgs) {
  return ajax("http://some.api/person", ...laterArgs);
};
```

O mesmo será verdade para `getOrder(..)`. Mas e quanto a `getCurrentUser(..)`?

```js
// versão 1
var getCurrentUser = partial(ajax, "http://some.api/person", {
  user: CURRENT_USER_ID,
});

// versão 2
var getCurrentUser = partial(getPerson, { user: CURRENT_USER_ID });
```

Podemos definir `getCurrentUser(..)` com os argumentos `url` e `data` especificados diretamente (versão 1), ou definir `getCurrentUser(..)` como uma aplicação parcial da aplicação parcial `getPerson(..)`, especificando apenas o argumento `data` adicional (versão 2).

A versão 2 é um pouco mais limpa de expressar porque reutiliza algo já definido. Como tal, acho que se encaixa um pouco mais no espírito do FP.

Só para garantir que entendemos como essas duas versões funcionarão nos bastidores, elas parecem respectivamente algo como:

```js
// versão 1
var getCurrentUser = function partiallyApplied(...laterArgs) {
  return ajax(
    "http://some.api/person",
    { user: CURRENT_USER_ID },
    ...laterArgs
  );
};

// versão 2
var getCurrentUser = function outerPartiallyApplied(...outerLaterArgs) {
  var getPerson = function innerPartiallyApplied(...innerLaterArgs) {
    return ajax("http://some.api/person", ...innerLaterArgs);
  };

  return getPerson({ user: CURRENT_USER_ID }, ...outerLaterArgs);
};
```

Novamente, pare e releia esses trechos de código para garantir que você entende o que está acontecendo ali.

**Nota:** A versão 2 tem uma camada extra de envolvimento de função. Isso pode parecer estranho e desnecessário, mas esta é apenas uma daquelas coisas em FP com as quais você vai querer se sentir realmente confortável. Iremos envolver muitas camadas de funções umas sobre as outras à medida que progredimos pelo texto. Lembre-se, esta é programação _funcional_!

Vamos dar uma olhada em outro exemplo da utilidade da aplicação parcial. Considere uma função `add(..)` que recebe dois argumentos e os soma:

```js
function add(x, y) {
  return x + y;
}
```

Agora imagine que queremos pegar uma lista de números e adicionar um certo número a cada um deles. Usaremos a utilidade `map(..)` (veja Capítulo 9, "Map") integrada aos arrays JS:

```js
[1, 2, 3, 4, 5].map(function adder(val) {
  return add(3, val);
}); // [4,5,6,7,8]
```

A razão pela qual não podemos passar `add(..)` diretamente para `map(..)` é porque a assinatura de `add(..)` não corresponde à função de mapeamento que `map(..)` espera. É aí que a aplicação parcial pode nos ajudar: podemos adaptar a assinatura de `add(..)` para algo que coincida:

```js
[1, 2, 3, 4, 5].map(partial(add, 3)); // [4,5,6,7,8]
```

A chamada `partial(add,3)` produz uma nova função unária que espera apenas mais um argumento.

A utilidade `map(..)` percorrerá a matriz (`[1,2,3,4,5]`) e chamará repetidamente essa função unária, uma vez para cada um desses valores, respectivamente. Portanto, as chamadas feitas serão efetivamente `add(3,1)`, `add(3,2)`, `add(3,3)`, `add(3,4)` e `add(3,5)`. O array desses resultados é `[4,5,6,7,8]`.

### `bind(..)`

As funções JavaScript possuem uma utilidade integrada chamada `bind(..)`. Ela possui duas capacidades: pré-definir o contexto `this` e aplicar argumentos parcialmente.

Acredito que é extremamente equivocado confundir essas duas capacidades em uma única utilidade. Às vezes, você desejará vincular o contexto `this` de forma rígida e não aplicar argumentos parcialmente. Outras vezes, você desejará aplicar argumentos parcialmente, mas não se importar com a vinculação de `this`. Nunca precisei de ambas ao mesmo tempo.

O último cenário (aplicação parcial sem definir o contexto `this`) é estranho porque você precisa passar um espaço reservado ignorável para o argumento de vinculação de `this` (o primeiro), geralmente `null`.

Considere:

```js
var getPerson = ajax.bind(null, "http://some.api/person");
```

Esse `null` simplesmente me irrita profundamente. Apesar dessa irritação, é levemente conveniente que o JS tenha uma utilidade integrada para aplicação parcial. No entanto, a maioria dos programadores FP prefere usar a utilidade `partial(..)` dedicada em sua biblioteca FP escolhida.

### Invertendo Argumentos

Lembre-se que a assinatura para nossa função Ajax é: `ajax( url, data, cb )`. E se quiséssemos aplicar parcialmente o `cb` mas esperar para especificar `data` e `url` mais tarde? Poderíamos criar uma utilidade que envolve uma função para inverter a ordem de seus argumentos:

```js
function reverseArgs(fn) {
  return function argsReversed(...args) {
    return fn(...args.reverse());
  };
}

// ou a forma de seta ES6 =>
var reverseArgs =
  (fn) =>
  (...args) =>
    fn(...args.reverse());
```

Agora podemos inverter a ordem dos argumentos `ajax(..)`, para que possamos então aplicar parcialmente da direita em vez da esquerda. Para restaurar a ordem esperada, inverteremos, então, a função parcialmente aplicada subsequente:

```js
var cache = {};

var cacheResult = reverseArgs(
  partial(reverseArgs(ajax), function onResult(obj) {
    cache[obj.id] = obj;
  })
);

// Depois:
cacheResult("http://some.api/person", { user: CURRENT_USER_ID });
```

Em vez de usar manualmente `reverseArgs(..)` (duas vezes!) para este propósito, podemos definir um `partialRight(..)` que aplica parcialmente os argumentos mais à direita. Por baixo dos panos, ele pode usar o mesmo truque de dupla inversão:

<a name="partialright"></a>

```js
function partialRight(fn, ...presetArgs) {
  return reverseArgs(partial(reverseArgs(fn), ...presetArgs.reverse()));
}

var cacheResult = partialRight(ajax, function onResult(obj) {
  cache[obj.id] = obj;
});

// Depois:
cacheResult("http://some.api/person", { user: CURRENT_USER_ID });
```

Outra implementação de `partialRight(..)` mais direta (e certamente mais performante) que não usa o truque de dupla reversão:

```js
function partialRight(fn, ...presetArgs) {
  return function partiallyApplied(...laterArgs) {
    return fn(...laterArgs, ...presetArgs);
  };
}

// ou a forma de seta ES6 =>
var partialRight =
  (fn, ...presetArgs) =>
  (...laterArgs) =>
    fn(...laterArgs, ...presetArgs);
```

Nenhuma dessas implementações de `partialRight(..)` garante que um parâmetro específico receberá um valor parcialmente aplicado específico; apenas garante que o(s) valor(es) parcialmente aplicado(s) apareça(m) como o(s) argumento(s) mais à direita (ou seja, último(s)) passado(s) para a função original.

Por exemplo:

```js
function foo(x, y, z, ...rest) {
  console.log(x, y, z, rest);
}

var f = partialRight(foo, "z:last");

f(1, 2); // 1 2 "z:last" []

f(1); // 1 "z:last" undefined []

f(1, 2, 3); // 1 2 3 ["z:last"]

f(1, 2, 3, 4); // 1 2 3 [4,"z:last"]
```

O valor "z:last" é aplicado apenas ao parâmetro z no caso em que f(..) é chamado com exatamente dois argumentos (correspondendo aos parâmetros x e y). Em todos os outros casos, "z:last" será apenas o argumento mais à direita, independentemente de quantos argumentos o precedam.

## Um de Cada Vez

Vamos examinar uma técnica semelhante à aplicação parcial, onde uma função que espera vários argumentos é decomposta em funções encadeadas sucessivas que cada uma recebe um único argumento (ariedade: 1) e retorna outra função para aceitar o próximo argumento.

Essa técnica é chamada de currying.

Para ilustrar primeiro, imagine que tivéssemos uma versão curried de ajax(..) já criada. É assim que a usaríamos:

```js
curriedAjax("http://some.api/person")({ user: CURRENT_USER_ID })(
  function foundUser(user) {
    /* .. */
  }
);
```

Os três conjuntos de `(..)`s denotam três chamadas de função encadeadas. Mas, talvez, separar cada uma das três chamadas ajude a ver melhor o que está acontecendo:

```js
var personFetcher = curriedAjax("http://some.api/person");

var getCurrentUser = personFetcher({ user: CURRENT_USER_ID });

getCurrentUser(function foundUser(user) {
  /* .. */
});
```

Em vez de receber todos os argumentos de uma vez (como `ajax(..)`), ou alguns dos argumentos adiantados e o resto depois (via `partial(..)`), esta função `curriedAjax(..)` recebe um argumento por vez, cada um em uma chamada de função separada.

Currying é semelhante à aplicação parcial no sentido de que cada chamada curried subsequente aplica parcialmente outro argumento à função original, até que todos os argumentos tenham sido passados.

A principal diferença é que `curriedAjax(..)` retornará uma função (chamamos de `personFetcher(..)`), que espera **apenas o próximo argumento** `data`, não uma que (como a `getPerson(..)` anterior) pode receber todos os outros argumentos.

Se uma função original esperasse cinco argumentos, a forma curried dessa função receberia apenas o primeiro argumento e retornaria uma função para aceitar o segundo. Essa função receberia apenas o segundo argumento e retornaria uma função para aceitar o terceiro. E assim por diante.

Portanto, o currying desfaz uma única função de alta ariedade em uma série de funções unárias encadeadas.

Como podemos definir uma utilidade para fazer esse currying? Considere:

<a name="curry"></a>

```js
function curry(fn, arity = fn.length) {
  return (function nextCurried(prevArgs) {
    return function curried(nextArg) {
      var args = [...prevArgs, nextArg];

      if (args.length >= arity) {
        return fn(...args);
      } else {
        return nextCurried(args);
      }
    };
  })([]);
}

// ou a forma de seta ES6 =>
var curry = (fn, arity = fn.length, nextCurried) =>
  (nextCurried = (prevArgs) => (nextArg) => {
    var args = [...prevArgs, nextArg];

    if (args.length >= arity) {
      return fn(...args);
    } else {
      return nextCurried(args);
    }
  })([]);
```

A abordagem aqui é iniciar uma coleção de argumentos em `prevArgs` como um array `[]` vazio, e adicionar cada `nextArg` recebido a ele, chamando a concatenação `args`. Enquanto `args.length` for menor que `arity` (o número de parâmetros declarados/esperados da função original `fn(..)`), crie e retorne outra função `curried(..)` para coletar o próximo argumento `nextArg`, passando a coleção `args` em execução como seu `prevArgs`. Uma vez que tenhamos argumentos `args` suficientes, execute a função original `fn(..)` com eles.

Por padrão, esta implementação depende da capacidade de inspecionar a propriedade `length` da função a ser currificada para saber quantas iterações de currificação serão necessárias antes de coletarmos todos os seus argumentos esperados.

**Nota:** Se você usar esta implementação de `curry(..)` com uma função que não possui uma propriedade `length` precisa, precisará passar o `arity` (o segundo parâmetro de `curry(..)`) para garantir que `curry(..)` funcione corretamente. `length` será impreciso se a assinatura do parâmetro da função incluir valores de parâmetro padrão, desestruturação de parâmetro ou for variádica com `...args` (consulte Capítulo 2).

Aqui está como usaríamos `curry(..)` para nosso exemplo anterior de `ajax(..)`:

```js
var curriedAjax = curry(ajax);

var personFetcher = curriedAjax("http://some.api/person");

var getCurrentUser = personFetcher({ user: CURRENT_USER_ID });

getCurrentUser(function foundUser(user) {
  /* .. */
});
```

Cada chamada aplica parcialmente mais um argumento à chamada original `ajax(..)`, até que todos os três tenham sido fornecidos e `ajax(..)` seja realmente invocado.

Lembre-se do nosso exemplo da discussão sobre aplicação parcial sobre adicionar `3` a cada valor em uma lista de números? Como a currying é semelhante à aplicação parcial, poderíamos fazer essa tarefa com currying quase da mesma maneira:

```js
[1, 2, 3, 4, 5].map(curry(add)(3)); // [4,5,6,7,8]
```

A diferença entre os dois? `partial(add,3)` vs `curry(add)(3)`.

Por que você pode escolher `curry(..)` em vez de `partial(..)`? Pode ser útil no caso em que você sabe de antemão que `add(..)` é a função a ser adaptada, mas o valor `3` ainda não é conhecido:

```js
var adder = curry(add);

// depois
[1, 2, 3, 4, 5].map(adder(3)); // [4,5,6,7,8]
```

Vamos ver outro exemplo de números, desta vez adicionando uma lista deles juntos:

```js
function sum(...nums) {
  var total = 0;
  for (let num of nums) {
    total += num;
  }
  return total;
}

sum(1, 2, 3, 4, 5); // 15

// agora com currying:
// (5 para indicar quantos devemos esperar)

var curriedSum = curry(sum, 5);

curriedSum(1)(2)(3)(4)(5); // 15
```

A vantagem do currying aqui é que cada chamada para passar um argumento produz outra função que é mais especializada, e podemos capturar e usar **essa** nova função mais tarde no programa. A aplicação parcial especifica todos os argumentos parcialmente aplicados antecipadamente, produzindo uma função que está esperando por todos os outros argumentos **na próxima chamada**.

Se você quisesse usar a aplicação parcial para especificar um parâmetro (ou vários!) de cada vez, teria que continuar chamando `partial(..)` novamente em cada função parcialmente aplicada sucessiva. Por outro lado, as funções currificadas fazem isso automaticamente, tornando o trabalho com argumentos individuais um de cada vez mais ergonômico.

Tanto o currying quanto a aplicação parcial usam o fechamento para lembrar os argumentos ao longo do tempo até que todos tenham sido recebidos, e então a função original pode ser invocada.

### Visualizing Curried Functions

Let's examine more closely the `curriedSum(..)` from the previous section. Recall its usage: `curriedSum(1)(2)(3)(4)(5)`; five subsequent (chained) function calls.

What if we manually defined a `curriedSum(..)` instead of using `curry(..)`? How would that look?

```js
function curriedSum(v1) {
  return function (v2) {
    return function (v3) {
      return function (v4) {
        return function (v5) {
          return sum(v1, v2, v3, v4, v5);
        };
      };
    };
  };
}
```

Definitely uglier, no question. But this is an important way to visualize what's going on with a curried function. Each nested function call is returning another function that's going to accept the next argument, and that continues until we've specified all the expected arguments.

When trying to decipher curried functions, I've found it helps me tremendously if I can unwrap them mentally as a series of nested functions.

In fact, to reinforce that point, let's consider the same code but written with ES6 arrow functions:

```js
curriedSum = (v1) => (v2) => (v3) => (v4) => (v5) => sum(v1, v2, v3, v4, v5);
```

And now, all on one line:

```js
curriedSum = (v1) => (v2) => (v3) => (v4) => (v5) => sum(v1, v2, v3, v4, v5);
```

Depending on your perspective, that form of visualizing the curried function may be more or less helpful to you. For me, it's a fair bit more obscured.

But the reason I show it that way is that it happens to look almost identical to the mathematical notation (and Haskell syntax) for a curried function! That's one reason why those who like mathematical notation (and/or Haskell) like the ES6 arrow function form.

### Why Currying and Partial Application?

With either style -- currying (such as `sum(1)(2)(3)`) or partial application (such as `partial(sum,1,2)(3)`) -- the call-site unquestionably looks stranger than a more common one like `sum(1,2,3)`. So **why would we ever go this direction** when adopting FP? There are multiple layers to answering that question.

The first and most obvious reason is that both currying and partial application allow you to separate in time/space (throughout your codebase) when and where separate arguments are specified, whereas traditional function calls require all the arguments to be present at the same time. If you have a place in your code where you'll know some of the arguments and another place where the other arguments are determined, currying or partial application are very useful.

Another layer to this answer, specifically for currying, is that composition of functions is much easier when there's only one argument. So a function that ultimately needs three arguments, if curried, becomes a function that needs just one, three times over. That kind of unary function will be a lot easier to work with when we start composing them. We'll tackle this topic later in [Chapter 4](ch4.md).

But the most important layer is specialization of generalized functions, and how such abstraction improves readability of code.

Consider our running `ajax(..)` example:

```js
ajax(
  "http://some.api/person",
  { user: CURRENT_USER_ID },
  function foundUser(user) {
    /* .. */
  }
);
```

The call-site includes all the information necessary to pass to the most generalized version of the utility (`ajax(..)`). The potential readability downside is that it may be the case that the URL and the data are not relevant information at this point in the program, but yet that information is cluttering up the call-site nonetheless.

Now consider:

```js
var getCurrentUser = partial(ajax, "http://some.api/person", {
  user: CURRENT_USER_ID,
});

// later

getCurrentUser(function foundUser(user) {
  /* .. */
});
```

In this version, we define a `getCurrentUser(..)` function ahead of time that already has known information like URL and data preset. The call-site for `getCurrentUser(..)` then isn't cluttered by information that **at that point of the code** isn't relevant.

Moreover, the semantic name for the function `getCurrentUser(..)` more accurately depicts what is happening than just `ajax(..)` with a URL and data would.

That's what abstraction is all about: separating two sets of details -- in this case, the _how_ of getting a current user and the _what_ we do with that user -- and inserting a semantic boundary between them, which eases the reasoning of each part independently.

Whether you use currying or partial application, creating specialized functions from generalized ones is a powerful technique for semantic abstraction and improved readability.

### Currying More Than One Argument?

The definition and implementation I've given of currying thus far is, I believe, as true to the spirit as we can likely get in JavaScript.

Specifically, if we look briefly at how currying works in Haskell, we can observe that multiple arguments always go in to a function one at a time, one per curried call -- other than tuples (analogous to arrays for our purposes) that transport multiple values in a single argument.

For example, in Haskell:

```haskell
foo 1 2 3
```

This calls the `foo` function, and has the result of passing in three values `1`, `2`, and `3`. But functions are automatically curried in Haskell, which means each value goes in as a separate curried-call. The JS equivalent of that would look like `foo(1)(2)(3)`, which is the same style as the `curry(..)` I presented earlier.

**Note:** In Haskell, `foo (1,2,3)` is not passing in those three values at once as three separate arguments, but a tuple (kinda like a JS array) as a single argument. To work, `foo` would need to be altered to handle a tuple in that argument position. As far as I can tell, there's no way in Haskell to pass all three arguments separately with just one function call; each argument gets its own curried-call. Of course, the presence of multiple calls is transparent to the Haskell developer, but it's a lot more syntactically obvious to the JS developer.

For these reasons, I think the `curry(..)` that I demonstrated earlier is a faithful adaptation, or what I might call "strict currying". However, it's important to note that there's a looser definition used in most popular JavaScript FP libraries.

Specifically, JS currying utilities typically allow you to specify multiple arguments for each curried-call. Revisiting our `sum(..)` example from before, this would look like:

```js
var curriedSum = looseCurry(sum, 5);

curriedSum(1)(2, 3)(4, 5); // 15
```

We see a slight syntax savings of fewer `( )`, and an implied performance benefit of now having three function calls instead of five. But other than that, using `looseCurry(..)` is identical in end result to the narrower `curry(..)` definition from earlier. I would guess the convenience/performance factor is probably why frameworks allow multiple arguments. This seems mostly like a matter of taste.

We can adapt our previous currying implementation to this common looser definition:

<a name="loosecurry"></a>

```js
function looseCurry(fn, arity = fn.length) {
  return (function nextCurried(prevArgs) {
    return function curried(...nextArgs) {
      var args = [...prevArgs, ...nextArgs];

      if (args.length >= arity) {
        return fn(...args);
      } else {
        return nextCurried(args);
      }
    };
  })([]);
}
```

Now each curried-call accepts one or more arguments (as `nextArgs`). We'll leave it as an exercise for the interested reader to define the ES6 `=>` version of `looseCurry(..)` similar to how we did it for `curry(..)` earlier.

### No Curry for Me, Please

It may also be the case that you have a curried function that you'd like to essentially un-curry -- basically, to turn a function like `f(1)(2)(3)` back into a function like `g(1,2,3)`.

The standard utility for this is (un)shockingly typically called `uncurry(..)`. Here's a simple naive implementation:

```js
function uncurry(fn) {
  return function uncurried(...args) {
    var ret = fn;

    for (let arg of args) {
      ret = ret(arg);
    }

    return ret;
  };
}

// or the ES6 => arrow form
var uncurry =
  (fn) =>
  (...args) => {
    var ret = fn;

    for (let arg of args) {
      ret = ret(arg);
    }

    return ret;
  };
```

**Warning:** Don't just assume that `uncurry(curry(f))` has the same behavior as `f`. In some libraries the uncurrying would result in a function like the original, but not all of them; certainly our example here does not. The uncurried function acts (mostly) the same as the original function if you pass as many arguments to it as the original function expected. However, if you pass fewer arguments, you still get back a partially curried function waiting for more arguments; this quirk is illustrated in the following snippet:

```js
function sum(...nums) {
  var sum = 0;
  for (let num of nums) {
    sum += num;
  }
  return sum;
}

var curriedSum = curry(sum, 5);
var uncurriedSum = uncurry(curriedSum);

curriedSum(1)(2)(3)(4)(5); // 15

uncurriedSum(1, 2, 3, 4, 5); // 15
uncurriedSum(1, 2, 3)(4)(5); // 15
```

Probably the more common case of using `uncurry(..)` is not with a manually curried function as just shown, but with a function that comes out curried as a result of some other set of operations. We'll illustrate that scenario later in this chapter in the ["No Points" discussion](#no-points).

## Order Matters

In Chapter 2, we explored the [named arguments pattern](ch2.md/#named-arguments). One primary advantage of named arguments is not needing to juggle argument ordering, thereby improving readability.

We've looked at the advantages of using currying/partial application to provide individual arguments to a function separately. But the downside is that these techniques are traditionally based on positional arguments; argument ordering is thus an inevitable headache.

Utilities like `reverseArgs(..)` (and others) are necessary to juggle arguments to get them into the right order. Sometimes we get lucky and define a function with parameters in the order that we later want to curry them, but other times that order is incompatible and we have to jump through hoops to reorder.

The frustration is not merely that we need to use some utility to juggle the properties, but the fact that the usage of the utility clutters up our code a bit with extra noise. These kinds of things are like little paper cuts; one here or there isn't a showstopper, but the pain can certainly add up.

Can we improve currying/partial application to free it from these ordering concerns? Let's apply the tricks from named arguments style and invent some helper utilities for this adaptation:

```js
function partialProps(fn, presetArgsObj) {
  return function partiallyApplied(laterArgsObj) {
    return fn(Object.assign({}, presetArgsObj, laterArgsObj));
  };
}

function curryProps(fn, arity = 1) {
  return (function nextCurried(prevArgsObj) {
    return function curried(nextArgObj = {}) {
      var [key] = Object.keys(nextArgObj);
      var allArgsObj = Object.assign({}, prevArgsObj, {
        [key]: nextArgObj[key],
      });

      if (Object.keys(allArgsObj).length >= arity) {
        return fn(allArgsObj);
      } else {
        return nextCurried(allArgsObj);
      }
    };
  })({});
}
```

**Tip:** We don't even need a `partialPropsRight(..)` because we don't need to care about what order properties are being mapped; the name mappings make that ordering concern moot!

Here's how to use those helpers:

```js
function foo({ x, y, z } = {}) {
  console.log(`x:${x} y:${y} z:${z}`);
}

var f1 = curryProps(foo, 3);
var f2 = partialProps(foo, { y: 2 });

f1({ y: 2 })({ x: 1 })({ z: 3 });
// x:1 y:2 z:3

f2({ z: 3, x: 1 });
// x:1 y:2 z:3
```

Even with currying or partial application, order doesn't matter anymore! We can now specify which arguments we want in whatever sequence makes sense. No more `reverseArgs(..)` or other nuisances. Cool!

**Tip:** If this style of function arguments seems useful or interesting to you, check out coverage of my [FPO library in Appendix C](apC.md/#bonus-fpo).

### Spreading Properties

Unfortunately, we can only take advantage of currying with named arguments if we have control over the signature of `foo(..)` and define it to destructure its first parameter. What if we wanted to use this technique with a function that had its parameters individually listed (no parameter destructuring!), and we couldn't change that function signature? For example:

```js
function bar(x, y, z) {
  console.log(`x:${x} y:${y} z:${z}`);
}
```

Just like the `spreadArgs(..)` utility earlier, we can define a `spreadArgProps(..)` helper that takes the `key: value` pairs out of an object argument and "spreads" the values out as individual arguments.

There are some quirks to be aware of, though. With `spreadArgs(..)`, we were dealing with arrays, where ordering is well defined and obvious. However, with objects, property order is less clear and not necessarily reliable. Depending on how an object is created and properties set, we cannot be absolutely certain what enumeration order properties would come out.

Such a utility needs a way to let you define what order the function in question expects its arguments (e.g., property enumeration order). We can pass an array like `["x","y","z"]` to tell the utility to pull the properties off the object argument in exactly that order.

That's decent, but it's also unfortunate that it then _obligates_ us to add that property-name array even for the simplest of functions. Is there any kind of trick we could use to detect what order the parameters are listed for a function, in at least the common simple cases? Fortunately, yes!

JavaScript functions have a `.toString()` method that gives a string representation of the function's code, including the function declaration signature. Dusting off our regular expression parsing skills, we can parse the string representation of the function, and pull out the individually named parameters. The code looks a bit gnarly, but it's good enough to get the job done:

```js
function spreadArgProps(
    fn,
    propOrder =
        fn.toString()
        .replace( /^(?:(?:function.*\(([^]*?)\))|(?:([^\(\)]+?)
            \s*=>)|(?:\(([^]*?)\)\s*=>))[^]+$/, "$1$2$3" )
        .split( /\s*,\s*/ )
        .map( v => v.replace( /[=\s].*$/, "" ) )
) {
    return function spreadFn(argsObj){
        return fn( ...propOrder.map( k => argsObj[k] ) );
    };
}
```

**Note:** This utility's parameter parsing logic is far from bullet-proof; we're using regular expressions to parse code, which is already a faulty premise! But our only goal here is to handle the common cases, which this does reasonably well. We only need a sensible default detection of parameter order for functions with simple parameters (including those with default parameter values). We don't, for example, need to be able to parse out a complex destructured parameter, because we wouldn't likely be using this utility with such a function, anyway. So, this logic gets the job done 80% of the time; it lets us override the `propOrder` array for any other more complex function signature that wouldn't otherwise be correctly parsed. That's the kind of pragmatic balance this book seeks to find wherever possible.

Let's illustrate using our `spreadArgProps(..)` utility:

```js
function bar(x, y, z) {
  console.log(`x:${x} y:${y} z:${z}`);
}

var f3 = curryProps(spreadArgProps(bar), 3);
var f4 = partialProps(spreadArgProps(bar), { y: 2 });

f3({ y: 2 })({ x: 1 })({ z: 3 });
// x:1 y:2 z:3

f4({ z: 3, x: 1 });
// x:1 y:2 z:3
```

While order is no longer a concern, usage of functions defined in this style requires you to know what each argument's exact name is. You can't just remember, "oh, the function goes in as the first argument" anymore. Instead, you have to remember, "the function parameter is called 'fn'." Conventions can create consistency of naming that lessens this burden, but it's still something to be aware of.

Weigh these trade-offs carefully.

## No Points

A popular style of coding in the FP world aims to reduce some of the visual clutter by removing unnecessary parameter-argument mapping. This style is formally called tacit programming, or more commonly: point-free style. The term "point" here is referring to a function's parameter input.

**Warning:** Stop for a moment. Let's make sure we're careful not to take this discussion as an unbounded suggestion that you go overboard trying to be point-free in your FP code at all costs. This should be a technique for improving readability, when used in moderation. But as with most things in software development, you can definitely abuse it. If your code gets harder to understand because of the hoops you have to jump through to be point-free, stop. You won't win a blue ribbon just because you found some clever but esoteric way to remove another "point" from your code.

Let's start with a simple example:

```js
function double(x) {
  return x * 2;
}

[1, 2, 3, 4, 5].map(function mapper(v) {
  return double(v);
});
// [2,4,6,8,10]
```

Can you see that `mapper(..)` and `double(..)` have the same (or compatible, anyway) signatures? The parameter ("point") `v` can directly map to the corresponding argument in the `double(..)` call. As such, the `mapper(..)` function wrapper is unnecessary. Let's simplify with point-free style:

```js
function double(x) {
  return x * 2;
}

[1, 2, 3, 4, 5].map(double);
// [2,4,6,8,10]
```

Let's revisit an example from earlier:

```js
["1", "2", "3"].map(function mapper(v) {
  return parseInt(v);
});
// [1,2,3]
```

In this example, `mapper(..)` is actually serving an important purpose, which is to discard the `index` argument that `map(..)` would pass in, because `parseInt(..)` would incorrectly interpret that value as a `radix` for the parsing.

If you recall from the beginning of this chapter, this was an example where `unary(..)` helps us out:

```js
["1", "2", "3"].map(unary(parseInt));
// [1,2,3]
```

Point-free!

The key thing to look for is if you have a function with parameter(s) that is/are directly passed to an inner function call. In both of the preceding examples, `mapper(..)` had the `v` parameter that was passed along to another function call. We were able to replace that layer of abstraction with a point-free expression using `unary(..)`.

**Warning:** You might have been tempted, as I was, to try `map(partialRight(parseInt,10))` to right-partially apply the `10` value as the `radix`. However, as we saw earlier, `partialRight(..)` only guarantees that `10` will be the last argument passed in, not that it will be specifically the second argument. Since `map(..)` itself passes three arguments (`value`, `index`, `arr`) to its mapping function, the `10` value would just be the fourth argument to `parseInt(..)`; it only pays attention to the first two.

<a name="shortlongenough"></a>

Here's another example:

```js
// convenience to avoid any potential binding issue
// with trying to use `console.log` as a function
function output(txt) {
  console.log(txt);
}

function printIf(predicate, msg) {
  if (predicate(msg)) {
    output(msg);
  }
}

function isShortEnough(str) {
  return str.length <= 5;
}

var msg1 = "Hello";
var msg2 = msg1 + " World";

printIf(isShortEnough, msg1); // Hello
printIf(isShortEnough, msg2);
```

Now let's say you want to print a message only if it's long enough; in other words, if it's `!isShortEnough(..)`. Your first thought is probably this:

```js
function isLongEnough(str) {
  return !isShortEnough(str);
}

printIf(isLongEnough, msg1);
printIf(isLongEnough, msg2); // Hello World
```

Easy enough... but "points" now! See how `str` is passed through? Without re-implementing the `str.length` check, can we refactor this code to point-free style?

Let's define a `not(..)` negation helper (often referred to as `complement(..)` in FP libraries):

```js
function not(predicate) {
  return function negated(...args) {
    return !predicate(...args);
  };
}

// or the ES6 => arrow form
var not =
  (predicate) =>
  (...args) =>
    !predicate(...args);
```

Next, let's use `not(..)` to alternatively define `isLongEnough(..)` without "points":

```js
var isLongEnough = not(isShortEnough);

printIf(isLongEnough, msg2); // Hello World
```

That's pretty good, isn't it? But we _could_ keep going. `printIf(..)` could be refactored to be point-free itself.

We can express the `if` conditional part with a `when(..)` utility:

```js
function when(predicate, fn) {
  return function conditional(...args) {
    if (predicate(...args)) {
      return fn(...args);
    }
  };
}

// or the ES6 => form
var when =
  (predicate, fn) =>
  (...args) =>
    predicate(...args) ? fn(...args) : undefined;
```

Let's mix `when(..)` with a few other helper utilities we've seen earlier in this chapter, to make the point-free `printIf(..)`:

```js
var printIf = uncurry(partialRight(when, output));
```

Here's how we did it: we right-partially-applied the `output` method as the second (`fn`) argument for `when(..)`, which leaves us with a function still expecting the first argument (`predicate`). _That_ function when called produces another function expecting the message string; it would look like this: `fn(predicate)(str)`.

A chain of multiple (two) function calls like that looks an awful lot like a curried function, so we `uncurry(..)` this result to produce a single function that expects the two `str` and `predicate` arguments together, which matches the original `printIf(predicate,str)` signature.

Here's the whole example put back together (assuming various utilities we've already detailed in this chapter are present):

<a name="finalshortlong"></a>

```js
function output(msg) {
  console.log(msg);
}

function isShortEnough(str) {
  return str.length <= 5;
}

var isLongEnough = not(isShortEnough);

var printIf = uncurry(partialRight(when, output));

var msg1 = "Hello";
var msg2 = msg1 + " World";

printIf(isShortEnough, msg1); // Hello
printIf(isShortEnough, msg2);

printIf(isLongEnough, msg1);
printIf(isLongEnough, msg2); // Hello World
```

Hopefully the FP practice of point-free style coding is starting to make a little more sense. It'll still take a lot of practice to train yourself to think this way naturally. **And you'll still have to make judgement calls** as to whether point-free coding is worth it, as well as what extent will benefit your code's readability.

What do you think? Points or no points for you?

**Note:** Want more practice with point-free style coding? We'll revisit this technique in [Chapter 4, "Revisiting Points"](ch4.md/#revisiting-points), based on newfound knowledge of function composition.

## Summary

Partial application is a technique for reducing the arity (that is, the expected number of arguments to a function) by creating a new function where some of the arguments are preset.

Currying is a special form of partial application where the arity is reduced to 1, with a chain of successive chained function calls, each which takes one argument. Once all arguments have been specified by these function calls, the original function is executed with all the collected arguments. You can also undo a currying.

Other important utilities like `unary(..)`, `identity(..)`, and `constant(..)` are part of the base toolbox for FP.

Point-free is a style of writing code that eliminates unnecessary verbosity of mapping parameters ("points") to arguments, with the goal of making code easier to read/understand.

All of these techniques twist functions around so they can work together more naturally. With your functions shaped compatibly now, the next chapter will teach you how to combine them to model the flows of data through your program.
