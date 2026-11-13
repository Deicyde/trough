---
declaration: section
origin: cited
lean: MetaMathlibExt.fibSubst, MetaMathlibExt.fibMorph, MetaMathlibExt.fibWord, MetaMathlibExt.fibInf, MetaMathlibExt.fibMorph_append, MetaMathlibExt.fibMorph_length_ge, MetaMathlibExt.fibWord_head, MetaMathlibExt.fibWord_length
statement: formalized
proof: formalized
---

# Fibonacci word

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html).

## Fibonacci substitution

The Fibonacci substitution sends each letter of the binary
alphabet $\{0, 1\}$ to a finite binary word: it maps $0$ to $01$ and $1$ to $0$.

The letters $0$ and $1$ are represented by the Booleans false and true.

Formalized by `MetaMathlibExt.fibSubst`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-subst).

## Fibonacci morphism

The Fibonacci morphism $\varphi$ extends the Fibonacci substitution
$\sigma$, which maps $0$ to $01$ and $1$ to $0$, to finite binary words by concatenation: $\varphi$
maps the empty word to the empty word, and $\varphi(bw) = \sigma(b)\varphi(w)$ for every letter
$b$ and every finite binary word $w$.

Formalized by `MetaMathlibExt.fibMorph`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-morph).

## Finite Fibonacci words

The finite Fibonacci words $f_n$, for natural numbers $n$, are
the words in the letters $0$ and $1$ defined by $f_0 = 0$ and $f_{n+1} = \varphi(f_n)$, where
$\varphi$ is the Fibonacci morphism, which replaces each letter $0$ by $01$ and each letter $1$
by $0$.

The first words are $0$, $01$, $010$, $01001$, $01001010$, and so on.

Formalized by `MetaMathlibExt.fibWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word).

## Infinite Fibonacci word

Let $f_0 = 0$ and let $f_{k+1}$ be the image of $f_k$ under the
Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$), so that $f_0, f_1, f_2, \ldots$ are the finite
Fibonacci words $0, 01, 010, 01001, \ldots$. The one-sided infinite Fibonacci word is the infinite
binary word whose letter at index $n$ (indices start at $0$) is the letter of $f_{n+2}$ at index
$n$.

Each $f_k$ is a prefix of $f_{k+1}$ and $f_{n+2}$ has more than $n$ letters, so this word is the
limit of the finite Fibonacci words.

Formalized by `MetaMathlibExt.fibInf`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-inf).

## The Fibonacci morphism respects concatenation

Let $\varphi$ be the Fibonacci morphism on
finite binary words, induced by $0 \mapsto 01$ and $1 \mapsto 0$. For all finite binary words $a$
and $b$, $\varphi(ab) = \varphi(a)\varphi(b)$, where juxtaposition denotes concatenation.

Formalized by `MetaMathlibExt.fibMorph_append`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-morph-append).

## The Fibonacci morphism does not shorten words

Let $\varphi$ be the Fibonacci morphism on
finite binary words, induced by $0 \mapsto 01$ and $1 \mapsto 0$. For every finite binary word $w$,
the length of $\varphi(w)$ is at least the length of $w$, that is, $|w| \le |\varphi(w)|$.

The reason is that every letter maps to a nonempty word.

Formalized by `MetaMathlibExt.fibMorph_length_ge`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-morph-length-ge).

## Finite Fibonacci words begin with $0$

Let $f_0 = 0$ and let $f_{k+1}$ be the image of
$f_k$ under the Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$). For every natural number $n$,
there is a finite binary word $t$ such that $f_n = 0t$, that is, the first letter of $f_n$ is $0$.

Formalized by `MetaMathlibExt.fibWord_head`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-head).

## Lower bound on the length of the finite Fibonacci words

Let $f_0 = 0$ and let $f_{k+1}$
be the image of $f_k$ under the Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$). For every
natural number $n$, the word $f_n$ has length at least $n + 1$.

Formalized by `MetaMathlibExt.fibWord_length`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-length).

## Consecutive finite Fibonacci words are nested

For every natural number $n$, the $n$-th
finite Fibonacci word $f_n$ is a prefix of $f_{n+1}$: there is a finite word $t$ in the letters
$0$ and $1$ with $f_{n+1} = f_n t$.

Formalized by `MetaMathlibExt.fibWord_nested_succ`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-nested-succ).

## Earlier finite Fibonacci words are prefixes of later ones

For all natural numbers
$n \le m$, the $n$-th finite Fibonacci word $f_n$ is a prefix of the $m$-th finite Fibonacci word
$f_m$: there is a finite word $t$ in the letters $0$ and $1$ with $f_m = f_n t$.

Formalized by `MetaMathlibExt.fibWord_prefix`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-prefix).

## Appending a word does not change earlier letters

Let $a$ and $t$ be finite words in the
letters $0$ and $1$, and let $k$ be a natural number smaller than the length of $a$. Then the
letter at position $k$ of the concatenation $a t$ equals the letter at position $k$ of $a$,
counting positions from $0$.

Formalized by `MetaMathlibExt.getD_append_prefix`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#get-d-append-prefix).

## Letters of the finite Fibonacci words stabilize

Let $f_0 = 0$ and let $f_{k+1}$ be the
image of $f_k$ under the Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$). For all natural
numbers $n \le m$ and every index $i$ less than the length of $f_n$ (indices start at $0$), the
letter of $f_m$ at index $i$ equals the letter of $f_n$ at index $i$.

Formalized by `MetaMathlibExt.fibWord_getD_eq`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-get-d-eq).

## The finite Fibonacci word of index $n + 2$ has more than $n$ letters

Let $f_0 = 0$ and
let $f_{k+1}$ be the image of $f_k$ under the Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$).
For every natural number $n$, the length of $f_{n+2}$ is greater than $n$.

Formalized by `MetaMathlibExt.fibInf_bound`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-inf-bound).

## Finite Fibonacci words agree with the infinite Fibonacci word

Let $f_0 = 0$ and let
$f_{k+1}$ be the image of $f_k$ under the Fibonacci morphism ($0 \mapsto 01$, $1 \mapsto 0$). For
all natural numbers $m$ and $n$ such that $n$ is less than the length of $f_m$, the letter of $f_m$
at index $n$ equals the letter at index $n$ of the one-sided infinite Fibonacci word (indices start
at $0$). In other words, every $f_m$ is a prefix of the infinite Fibonacci word.

Formalized by `MetaMathlibExt.fibInf_agrees`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/FibonacciWord.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-inf-agrees).

## Recurrence for the finite Fibonacci words

Let $f_0, f_1, f_2, \ldots$ be the finite
Fibonacci words. For every natural number $n$, $f_{n+2} = f_{n+1} f_n$, where juxtaposition
denotes concatenation.

Formalized by `MetaMathlibExt.fibWord_add_two`, a theorem declared in [MathlibExt/Combinatorics/Words/FibonacciFactorization.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FibonacciFactorization.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-add-two).

## Concatenating the finite Fibonacci words

For every natural number $N$, prepending the
letters $0$ and $1$ to the concatenation $f_0 f_1 \cdots f_{N-1}$ of the first $N$ finite Fibonacci
words gives $f_{N+1}$: that is, $0\,1\,f_0 f_1 \cdots f_{N-1} = f_{N+1}$, where the concatenation
is empty when $N = 0$.

Formalized by `MetaMathlibExt.fibWord_factorization`, a theorem declared in [MathlibExt/Combinatorics/Words/FibonacciFactorization.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FibonacciFactorization.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-factorization).

## Finite Fibonacci words are prefixes of the infinite Fibonacci word

For every natural
number $n$, the finite Fibonacci word $f_n$ is the word formed by the first $|f_n|$ letters of the
infinite Fibonacci word.

Formalized by `MetaMathlibExt.fibWord_eq_ofFn_fibInf`, a theorem declared in [MathlibExt/Combinatorics/Words/FibonacciFactorization.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FibonacciFactorization.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-word-eq-of-fn-fib-inf).

## Factorization of the infinite Fibonacci word into finite Fibonacci words

Let $f$ be the
infinite Fibonacci word and let $f_0, f_1, f_2, \ldots$ be the finite Fibonacci words. For every
natural number $N$, the finite word $w_N = 0\,1\,f_0 f_1 \cdots f_{N-1}$ (so $w_0 = 01$) consists of
the first $|w_N|$ letters of $f$, and for every natural number $k$ the first $k$ letters of $f$
form a prefix of $w_N$ for some $N$. In this sense
$f = 0 \cdot 1 \cdot f_0 \cdot f_1 \cdot f_2 \cdots$.

## Sources

- Gabriele Fici, "Factorizations of the Fibonacci Infinite Word", Journal of Integer Sequences 18 (2015), Article 15.9.3, equation `fibo`.

Formalized by `MetaMathlibExt.fibInf_factorization`, a theorem declared in [MathlibExt/Combinatorics/Words/FibonacciFactorization.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FibonacciFactorization.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fib-inf-factorization).

## The infinite Fibonacci word as $0$ followed by the finite Fibonacci words

Let $f$ be an
infinite word over $\{0, 1\}$ and let $f_1, f_2, f_3, \ldots$ be finite words over $\{0, 1\}$ with
$f_1 = 1$, $f_2 = 0$ and $f_{n+3} = f_{n+2} f_{n+1}$ for every natural number $n$, such that for
every natural number $n$ the word $f_{n+2}$ consists of the first $|f_{n+2}|$ letters of $f$.
Then for every natural number $N$ the word $w_N = 0\,f_1 f_2 \cdots f_N$ (so $w_0 = 0$) consists of
the first $|w_N|$ letters of $f$, and for every natural number $k$ the first $k$ letters of $f$
form a prefix of $w_N$ for some $N$. In this sense $f = 0 \cdot f_1 \cdot f_2 \cdot f_3 \cdots$.

## Sources

- Gabriele Fici, "Factorizations of the Fibonacci Infinite Word", Journal of Integer Sequences 18 (2015), Article 15.9.3, Proposition lines 188-195 (equation `fibo`), <https://cs.uwaterloo.ca/journals/JIS/VOL18/Fici/fici5.tex>.

Formalized by `MetaMathlibExt.fibonacci_infinite_word_factorization`, a theorem declared in [MathlibExt/Combinatorics/Words/FibonacciFactorization.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FibonacciFactorization.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#fibonacci-infinite-word-factorization).

## Kimberling's set modulo 2 is the Fibonacci word

Let $K$ be the set of natural numbers
obtained from $1$ by finitely many applications of the maps $x \mapsto 2x$ and
$x \mapsto 4x - 1$. Let $S$ be a strictly increasing sequence of natural numbers whose set
of values is $K$, and let $w$ be the binary sequence with $w(n) = 1$ if $S(n + 1)$ is odd
and $w(n) = 0$ if $S(n + 1)$ is even. Let $\varphi$ be the morphism of binary words with
$\varphi(0) = 01$ and $\varphi(1) = 0$. Then for every $k \ge 0$, the first
$|\varphi^k(0)|$ terms $w(0) w(1) \cdots$ of $w$ spell the word $\varphi^k(0)$. In other
words, $S$ modulo $2$ with its first term dropped is the infinite Fibonacci word.

The source gives a third proof of this theorem of Kimberling, via a transducer
construction; Allouche and Shallit also reproved it.

## Sources

- Tomi Kärki, Anne Lacroix, and Michel Rigo, "On the Recognizability of Self-Generating Sets," Journal of Integer Sequences 13 (2010), Article 10.2.2, Theorem (section Kimberling set and the Fibonacci word, label secKF), lines 710–714, https://cs.uwaterloo.ca/journals/JIS/VOL13/Rigo/rigo6.tex

Formalized by `MetaMathlibExt.kimberling_set_mod_two_fibonacci_word`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/KimberlingFibonacciWord.lean, line 751](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/KimberlingFibonacciWord.lean#L751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html#kimberling-set-mod-two-fibonacci-word).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci word](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/fibonacci-word)
