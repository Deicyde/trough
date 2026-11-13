---
declaration: section
origin: cited
lean: MetaMathlibExt.hofstadterFAux, MetaMathlibExt.hofstadterF, MetaMathlibExt.hofstadterFAux_le, MetaMathlibExt.hofstadterF_zero, MetaMathlibExt.hofstadterF_eq, MetaMathlibExt.hofstadterF_small_values, MetaMathlibExt.hofTau, MetaMathlibExt.hofTauList
statement: formalized
---

# Generalized Hofstadter functions

53 results, 28 proved and 25 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html).

## Fuel-bounded generalized Hofstadter recursion

For natural numbers $k$, $p$ and $n$, the
value $A_k(p, n)$ is defined by recursion on the fuel $p$, which bounds the recursion depth:
$A_k(0, n) = 0$ and $A_k(p + 1, n) = n - g^k(n - 1)$, where $g^k$ is the $k$-fold iterate of the
function $g(m) = A_k(p, m)$ and both subtractions are truncated at $0$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.4 (Rocq definition `recf`).

Formalized by `MetaMathlibExt.hofstadterFAux`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-faux).

## Generalized Hofstadter function

For a natural number $k$, the function
$F_k : \mathbb{N} \to \mathbb{N}$ is given by $F_k(0) = 0$ and $F_k(n) = n - F_k^k(n - 1)$ for
$n \ge 1$, where $F_k^k$ is the $k$-fold iterate of $F_k$ (the identity when $k = 0$).

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.1.

Formalized by `MetaMathlibExt.hofstadterF`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f).

## The fuel-bounded Hofstadter recursion is bounded by its argument

For all natural numbers
$k$, $p$ and $n$, the fuel-bounded value $A_k(p, n)$ of the generalized Hofstadter recursion
satisfies $A_k(p, n) \le n$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.1 (`0 ≤ F_k(n) ≤ n`).

Formalized by `MetaMathlibExt.hofstadterFAux_le`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-faux-le).

## The generalized Hofstadter functions vanish at zero

For every natural number $k$, the
generalized Hofstadter function $F_k$ satisfies $F_k(0) = 0$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.1.

Formalized by `MetaMathlibExt.hofstadterF_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-zero).

## Recursion for the generalized Hofstadter function

For every $k \ge 0$ and every $n \ge 1$,
the generalized Hofstadter function $F_k$ satisfies $F_k(n) = n - F_k^k(n - 1)$, where $F_k^k$
is the $k$-fold iterate of $F_k$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.1.

Formalized by `MetaMathlibExt.hofstadterF_eq`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-eq).

## First values of Hofstadter's G and H

Let $F_k$ denote the generalized Hofstadter
functions. For $n = 0, 1, \dots, 10$ the values $F_2(n)$ are $0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6$
and the values $F_3(n)$ are $0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7$.

Here $F_2$ is Hofstadter's $G$ (OEIS A005206) and $F_3$ is Hofstadter's $H$ (OEIS A005374).

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Figure 1.

Formalized by `MetaMathlibExt.hofstadterF_small_values`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-small-values).

## The Hofstadter substitution on letters

For a natural number $k$, the substitution
$\tau_k$ sends the letter $k$ to the word $k\,1$ and every other letter $i \in \mathbb{N}$ to the
one-letter word $i + 1$.

The rule $i \mapsto i + 1$ is used only for $1 \le i < k$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2.

Formalized by `MetaMathlibExt.hofTau`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau).

## The Hofstadter substitution on finite words

For a natural number $k$, $\tau_k$ maps a
finite word $w$ over $\mathbb{N}$ to the concatenation, in order, of the words $\tau_k(a)$ for the
letters $a$ of $w$, where $\tau_k(k) = k\,1$ and $\tau_k(i) = i + 1$ for every letter $i \ne k$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2.

Formalized by `MetaMathlibExt.hofTauList`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau-list).

## Letter images under the generalized Hofstadter substitution are nonempty

For every
natural number $k$, let $\tau_k$ be the substitution on letters in $\mathbb{N}$ sending $k$ to
the two-letter word $k\,1$ and every other letter $m$ to the one-letter word $m + 1$. For every
natural number $i$, the image $\tau_k(i)$ of the letter $i$ has length at least $1$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (definition of `τ_k`).

Formalized by `MetaMathlibExt.one_le_length_hofTau`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#one-le-length-hof-tau).

## The generalized Hofstadter substitution does not shorten words

For every natural
number $k$, let $\tau_k$ be the substitution on letters in $\mathbb{N}$ sending $k$ to the
two-letter word $k\,1$ and every other letter $i$ to the one-letter word $i + 1$. For every
finite word $w$ over $\mathbb{N}$, the word $\tau_k(w)$, obtained by replacing each letter of
$w$ by its image under $\tau_k$, is at least as long as $w$: $|w| \le |\tau_k(w)|$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (definition of `τ_k`).

Formalized by `MetaMathlibExt.length_le_length_hofTauList`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#length-le-length-hof-tau-list).

## The Hofstadter substitution preserves prefixes

For a natural number $k$, let $\tau_k$ be
the morphism of finite words over $\mathbb{N}$ that replaces the letter $k$ by the word $k\,1$ and
every other letter $i$ by $i + 1$. For every $k$ and all finite words $u$, $v$ over $\mathbb{N}$,
if $u$ is a prefix of $v$, then $\tau_k(u)$ is a prefix of $\tau_k(v)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (`τ_k` is a morphism).

Formalized by `MetaMathlibExt.hofTauList_isPrefix`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau-list-is-prefix).

## Every iterate $\tau_k^j(k)$ starts with $k$

Let $\tau_k$ be the substitution sending the
letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, extended letterwise to words. For all
natural numbers $k$ and $j$, the word $\tau_k^j(k)$, obtained by applying $\tau_k$ to the
one-letter word $k$ a total of $j$ times, has the form $k\,r$ for some word $r$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (`τ_k(k) = k 1`).

Formalized by `MetaMathlibExt.exists_hofTauList_iterate_eq_cons`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#exists-hof-tau-list-iterate-eq-cons).

## Growth of the iterated generalized Hofstadter substitution

For natural numbers $k$
and $j$, let $\tau_k$ be the substitution on letters in $\mathbb{N}$ sending $k$ to the
two-letter word $k\,1$ and every other letter $i$ to the one-letter word $i + 1$, extended
letter by letter to finite words. The word $\tau_k^j(k)$, obtained by applying $\tau_k$
$j$ times to the one-letter word $k$, has length at least $j + 1$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (the fixed point `x_k` is the limit of `τ_k^j(k)`).

Formalized by `MetaMathlibExt.succ_le_length_hofTauList_iterate`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#succ-le-length-hof-tau-list-iterate).

## Consecutive iterates of the Hofstadter substitution on $k$ are nested

For a natural number
$k$, let $\tau_k$ be the morphism of finite words over $\mathbb{N}$ that replaces the letter $k$ by
the word $k\,1$ and every other letter $i$ by $i + 1$, and write $\tau_k^j(k)$ for the word
obtained by applying $\tau_k$ $j$ times to the one-letter word $k$. For all natural numbers $k$
and $j$, $\tau_k^j(k)$ is a prefix of $\tau_k^{j+1}(k)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (the fixed point `x_k` is the limit of `τ_k^j(k)`).

Formalized by `MetaMathlibExt.hofTauList_iterate_isPrefix_succ`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau-list-iterate-is-prefix-succ).

## The iterates of the Hofstadter substitution on $k$ form a chain of prefixes

For a natural
number $k$, let $\tau_k$ be the morphism of finite words over $\mathbb{N}$ that replaces the letter
$k$ by the word $k\,1$ and every other letter $i$ by $i + 1$, and write $\tau_k^j(k)$ for the word
obtained by applying $\tau_k$ $j$ times to the one-letter word $k$. For every natural number $k$
and all natural numbers $i \le j$, $\tau_k^i(k)$ is a prefix of $\tau_k^j(k)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (the fixed point `x_k` is the limit of `τ_k^j(k)`).

Formalized by `MetaMathlibExt.hofTauList_iterate_isPrefix`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau-list-iterate-is-prefix).

## Bounded growth of a word under $\tau_k$

Let $\tau_k$ be the substitution sending the
letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, extended letterwise to words. Given
$n$, a bound $f$ and a word $w$, the result is $w$ if $f = 0$ or $w$ has more than $n$ letters,
and otherwise it is the result for the bound $f - 1$ and the word $\tau_k(w)$. Thus $\tau_k$ is
applied to $w$ until the word has more than $n$ letters, at most $f$ times.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (prefixes `τ_k^j(k)` of `x_k`).

Formalized by `MetaMathlibExt.hofGrowAux`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-grow-aux).

## The shortest long iterate $\tau_k^j(k)$

Let $\tau_k$ be the substitution sending the
letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, extended letterwise to words. For
natural numbers $k$ and $n$, $\mathrm{grow}_k(n)$ is the word obtained from the one-letter word
$k$ by applying $\tau_k$ until it has more than $n$ letters, at most $n$ times. Since
$\tau_k^j(k)$ has at least $j + 1$ letters, this is the shortest iterate $\tau_k^j(k)$ with more
than $n$ letters.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (prefixes `τ_k^j(k)` of `x_k`).

Formalized by `MetaMathlibExt.hofGrow`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-grow).

## Growing from an iterate of $\tau_k$ gives an iterate of $\tau_k$

Let $\tau_k$ be the
substitution sending the letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, extended
letterwise to words, and let $\mathrm{grow}_{k,n}^f(w)$ be the word obtained from $w$ by applying
$\tau_k$ until it has more than $n$ letters, at most $f$ times. For all $k, n, f, j$ there is an
$m$ with $\mathrm{grow}_{k,n}^f(\tau_k^j(k)) = \tau_k^m(k)$ such that $\tau_k^m(k)$ has more than
$n$ letters or $j + f \le m$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (prefixes `τ_k^j(k)` of `x_k`).

Formalized by `MetaMathlibExt.hofGrowAux_iterate`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-grow-aux-iterate).

## The grown prefix is a long iterate of $\tau_k$

Let $\tau_k$ be the substitution sending
the letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, extended letterwise to words, and
let $\mathrm{grow}_k(n)$ be the word obtained from the one-letter word $k$ by applying $\tau_k$
until it has more than $n$ letters, at most $n$ times. For all natural numbers $k$ and $n$ there
is an $m$ with $\mathrm{grow}_k(n) = \tau_k^m(k)$, and $\mathrm{grow}_k(n)$ has more than $n$
letters.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (prefixes `τ_k^j(k)` of `x_k`).

Formalized by `MetaMathlibExt.exists_hofGrow_eq`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#exists-hof-grow-eq).

## Letters of the Hofstadter fixed-point word

For natural numbers $k$ and $n$, let $\tau_k$
be the substitution on letters in $\mathbb{N}$ that sends $k$ to the word $k\,1$ and every other
letter $i$ to $i + 1$, applied to words letter by letter, and let $\tau_k^j(k)$ be the word
obtained by applying $\tau_k$ $j$ times to the one-letter word $k$. Then $x_k[n]$ is the letter at
position $n$, counting from $0$, of the shortest word $\tau_k^j(k)$ with $j \ge 0$ that has more
than $n$ letters.

Since each word $\tau_k^j(k)$ is a prefix of $\tau_k^{j+1}(k)$, $x_k[n]$ is the letter at position
$n$ of the fixed point $x_k$ of $\tau_k$ that begins with $k$, and every word $\tau_k^j(k)$ with
more than $n$ letters has $x_k[n]$ at position $n$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2.

Formalized by `MetaMathlibExt.hofWord`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-word).

## Letters of $x_k$ from the iterates $\tau_k^j(k)$

For a natural number $k$, let $\tau_k$ be
the Hofstadter substitution on finite words over $\mathbb{N}$ ($k \mapsto k\,1$, $i \mapsto i + 1$
for $i \ne k$), let $x_k = x_k[0]\,x_k[1] \cdots$ be its fixed point, and write $\tau_k^j(k)$
for the word obtained by applying $\tau_k$ $j$ times to the one-letter word $k$. For all natural
numbers $k$, $n$ and $j$, if $\tau_k^j(k)$ has more than $n$ letters, then $x_k[n]$ is the letter
at position $n$ of $\tau_k^j(k)$, counting positions from $0$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2 (the fixed point `x_k` is the limit of `τ_k^j(k)`).

Formalized by `MetaMathlibExt.hofWord_eq_getElem`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-word-eq-get-elem).

## The letter $x_k(n)$ can be read off $\tau_k^n(k)$

For a natural number $k$, let $\tau_k$ be
the Hofstadter substitution on finite words over $\mathbb{N}$ ($k \mapsto k\,1$, $i \mapsto i + 1$
for $i \ne k$), let $x_k = x_k[0]\,x_k[1] \cdots$ be its fixed point, and write $\tau_k^n(k)$
for the word obtained by applying $\tau_k$ $n$ times to the one-letter word $k$. For all natural
numbers $k$ and $n$, $x_k[n]$ is the letter at position $n$ of $\tau_k^n(k)$, counting positions
from $0$ (this word has at least $n + 1$ letters).

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 1.2.

Formalized by `MetaMathlibExt.hofWord_eq_getElem_self`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-word-eq-get-elem-self).

## The prefix $x_k(0:n)$

For natural numbers $k$ and $n$, let $\tau_k$ be the
substitution $k \mapsto k\,1$, $i \mapsto i + 1$ for $i \ne k$, applied letter by letter to
words, and let $\tau_k^j$ be its $j$-fold iterate. Then $x_k[0:n)$ is the word formed by the
first $n$ letters of the shortest of the words $\tau_k^j(k)$, $j \ge 0$, that has more than $n$
letters.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 2.

Formalized by `MetaMathlibExt.hofPrefix`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-prefix).

## The prefix $x_k(0:n)$ letter by letter

Let $k$ and $n$ be natural numbers, let $x_k$ be
the fixed point of the substitution $\tau_k$ with letters $x_k[0], x_k[1], \dots$, and let
$x_k[0:n)$ be the word formed by the first $n$ letters of the shortest word $\tau_k^j(k)$ with
more than $n$ letters. Then $x_k[0:n) = x_k[0]\,x_k[1] \cdots x_k[n-1]$, the empty word when
$n = 0$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 2.

Formalized by `MetaMathlibExt.hofPrefix_eq_map`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-prefix-eq-map).

## The image length $L_k$

For natural numbers $k$ and $n$, $L_k(n) = |\tau_k(x_k[0:n))|$
is the length of the word obtained by applying the substitution $\tau_k$, letter by letter, to
the prefix $x_k[0:n)$ formed by the first $n$ letters of the fixed point $x_k$ of $\tau_k$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 2.

Formalized by `MetaMathlibExt.hofL`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l).

## Letter counts in the Hofstadter word

Let $x_k$ be the fixed point, starting with $k$, of
the substitution sending the letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, and write
$x_k[j]$ for its letter at index $j$. For a predicate $P$ on letters, $C_k^{(P)}(n)$ is the number
of letters satisfying $P$ in the prefix $x_k[0] \cdots x_k[n-1]$, that is,
$C_k^{(P)}(n) = \#\{0 \le j < n : P(x_k[j])\}$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 4.

Formalized by `MetaMathlibExt.hofCount`, a definition declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-count).

## Letter counts of the Hofstadter word as cardinalities

Let $x_k$ be the fixed point,
starting with $k$, of the substitution sending the letter $k$ to $k\,1$ and every other letter
$i$ to $i + 1$, and write $x_k[j]$ for its letter at index $j$. For every predicate $P$ on letters
and every $n$, the number $C_k^{(P)}(n)$ of letters satisfying $P$ in the prefix
$x_k[0] \cdots x_k[n-1]$ equals the number of indices $j < n$ with $P(x_k[j])$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Section 4.

Formalized by `MetaMathlibExt.hofCount_eq_card`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-count-eq-card).

## First values of $x_2$, $x_3$ and $L_2$

For a natural number $k$, let $x_k$ be the fixed
point of the Hofstadter substitution $\tau_k$ ($k \mapsto k\,1$, $i \mapsto i + 1$ for $i \ne k$),
and let $L_2(n)$ be the length of $\tau_2(x_2[0] \cdots x_2[n-1])$. The first eight letters of
the Fibonacci word $x_2$ are $2, 1, 2, 2, 1, 2, 1, 2$; the first eight letters of $x_3$ are
$3, 1, 2, 3, 3, 1, 3, 1$; and $L_2(0), \dots, L_2(5)$ are $0, 2, 3, 5, 7, 8$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Figure 2.

Formalized by `MetaMathlibExt.hofWord_small_values`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-word-small-values).

## Pointwise order of the generalized Hofstadter functions

For every $k \ge 1$ and every
natural number $n$, the generalized Hofstadter functions satisfy $F_k(n) \le F_{k+1}(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 1 (`jis-2026-26.3.3-thm-1`).

Stated but not proved: `MetaMathlibExt.hofstadterF_le_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-le-succ).

## Basic properties of the iterated Hofstadter functions

Let $j, k \ge 1$, let $F_k$ be the
generalized Hofstadter function, and write $F_k^i$ for its $i$-fold iterate. Then
$F_k^j(1) = F_k^j(2) = 1$; $F_k^j(n) \ge 1$ for every $n \ge 1$; $F_k^j(n) < n$ for every
$n \ge 2$; $F_k(n+1) - F_k(n) = 1 - \bigl(F_k^k(n) - F_k^k(n-1)\bigr)$ in $\mathbb{Z}$ for every
$n \ge 1$; $F_k^j(n+1)$ equals $F_k^j(n)$ or $F_k^j(n) + 1$ for every $n \ge 0$; and $F_k^j$ is
monotone and surjective from $\mathbb{N}$ to $\mathbb{N}$ but not injective.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 2 (`jis-2026-26.3.3-prop-2`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_basic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-basic).

## Iterates of the Hofstadter substitution on the letter $k$

Let $k \ge 1$, let $\tau_k$ be
the morphism of finite words over $\mathbb{N}$ that replaces the letter $k$ by the word $k\,1$ and
every other letter $i$ by $i + 1$, and write $\tau_k^j(k)$ for the word obtained by applying
$\tau_k$ $j$ times to the one-letter word $k$. For every natural number $j$: if $j \le k$, then
$\tau_k^j(k) = k\,1\,2 \cdots j$, the letter $k$ followed by $1, 2, \dots, j$; and if $j \ge k$,
then $\tau_k^j(k)$ is the concatenation $\tau_k^{j-1}(k)\,\tau_k^{j-k}(k)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 3 (`jis-2026-26.3.3-prop-3`).

Stated but not proved: `MetaMathlibExt.hofTauList_iterate_self` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-tau-list-iterate-self).

## Basic properties of the iterates of $L_k$

Let $k \ge 1$, let $x_k$ be the fixed point of
the substitution $\tau_k$, with letters $x_k[0], x_k[1], \dots$ and prefixes
$x_k[0:n) = x_k[0] \cdots x_k[n-1]$, let $L_k(n) = |\tau_k(x_k[0:n))|$, and write $f^j$ for the
$j$-fold iterate of a map $f$ (so $f^0$ is the identity). Then for every $j \ge 0$:
(1) $L_k^j(n) = |\tau_k^j(x_k[0:n))|$ for every $n$;
(2) $L_k^j(0) = 0$, and $L_k^j(n+1) = L_k^j(n) + |\tau_k^j(x_k[n])|$ for every $n$;
(3) $L_k^j(1) = j + 1$ if $j \le k$, and $L_k^j(1) = L_k^{j-1}(1) + L_k^{j-k}(1)$ if $j \ge k$;
(4) $n \mapsto L_k^j(n)$ is strictly increasing;
(5) $L_k^j(n) \ge n$ for every $n$, with equality if and only if $j = 0$ or $n = 0$;
(6) for every $n \ge 1$, the sequence $i \mapsto L_k^i(n)$ is strictly increasing.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 4 (`jis-2026-26.3.3-prop-4`).

Stated but not proved: `MetaMathlibExt.hofL_iterate_basic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-iterate-basic).

## Bracketing by the iterates of $L_k$

For $k \ge 1$, let $\tau_k$ be the substitution
sending the letter $k$ to $k\,1$ and every other letter $i$ to $i + 1$, let $x_k$ be its fixed
point starting with $k$, and let $L_k(n)$ be the length of the image under $\tau_k$ of the first
$n$ letters of $x_k$; write $L_k^j$ for the $j$-fold iterate of $L_k$. For all $j \ge 0$ and
$m \ge 1$ there is a unique $n \ge 1$ with $L_k^j(n - 1) < m \le L_k^j(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 5 (`jis-2026-26.3.3-prop-5`).

Stated but not proved: `MetaMathlibExt.existsUnique_hofL_iterate_bracket` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#exists-unique-hof-l-iterate-bracket).

## Fibres of the iterated Hofstadter functions

Let $k \ge 1$ and $j \ge 0$. Let $F_k$ be the
generalized Hofstadter function, let $x_k[0]\,x_k[1] \cdots$ be the fixed point, beginning with
$k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every other letter $i$ to $i + 1$,
let $L_k(m)$ be the length of the word $\tau_k(x_k[0] \cdots x_k[m-1])$, and write $f^j$ for the
$j$-fold iterate of a function $f$. Then for every $n \ge 1$, the set of $m$ with $F_k^j(m) = n$
is the interval $L_k^j(n-1) < m \le L_k^j(n)$; and for every $m \ge 1$,
$L_k^j(F_k^j(m) - 1) < m \le L_k^j(F_k^j(m))$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 6 (`jis-2026-26.3.3-thm-6`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_preimage_eq_Ioc` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-preimage-eq-ioc).

## Galois insertion between iterated Hofstadter functions

Let $k \ge 1$ and $j \ge 0$. Let
$F_k$ be the generalized Hofstadter function, let $x_k[0]\,x_k[1] \cdots$ be the fixed point,
beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every other letter
$i$ to $i + 1$, let $L_k(m)$ be the length of the word $\tau_k(x_k[0] \cdots x_k[m-1])$, and
write $f^j$ for the $j$-fold iterate of a function $f$. Then for all $n, m \ge 0$,
$F_k^j(n) \le m$ if and only if $n \le L_k^j(m)$, so $F_k^j$ and $L_k^j$ form a Galois
connection; and $F_k^j(L_k^j(m)) = m$ for every $m \ge 0$, so it is a Galois insertion.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Corollary 7 (`jis-2026-26.3.3-cor-7`).

Stated but not proved: `MetaMathlibExt.hofstadterF_hofL_galoisInsertion` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-hof-l-galois-insertion).

## Iterated Hofstadter functions as letter counts

Let $k \ge 1$ and $n \ge 0$. Let $F_k$ be
the generalized Hofstadter function and $F_k^j$ its $j$-fold iterate, let $x_k[0]\,x_k[1] \cdots$
be the fixed point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and
every other letter $i$ to $i + 1$, and for a property $P$ of letters let $C_k^{(P)}(m)$ be the
number of indices $0 \le i < m$ with $P(x_k[i])$. Then $F_k^{k-1}(n) = C_k^{(=k)}(n)$;
$F_k^j(n) = C_k^{(>j)}(n)$ for every $0 \le j < k$; and $F_k^{k+i-1}(n) = C_k^{(=i)}(n+i)$ for
every $1 \le i < k$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 8 (`jis-2026-26.3.3-prop-8`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_eq_hofCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-eq-hof-count).

## The image length $L_k$ as a letter count

Let $k \ge 1$. Let $F_k$ be the generalized
Hofstadter function and $F_k^{k-1}$ its $(k-1)$-fold iterate, let $x_k[0]\,x_k[1] \cdots$ be the
fixed point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, let $L_k(n)$ be the length of the word
$\tau_k(x_k[0] \cdots x_k[n-1])$, and let $C_k^{(=k)}(n)$ be the number of indices $0 \le i < n$
with $x_k[i] = k$. Then for every natural number $n$, $L_k(n) = n + C_k^{(=k)}(n)$ and
$L_k(n) = n + F_k^{k-1}(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 9 (`jis-2026-26.3.3-prop-9`).

Stated but not proved: `MetaMathlibExt.hofL_eq_add_hofCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-eq-add-hof-count).

## Generalized Hofstadter function as a letter count

Let $k > 1$ and $n \ge 0$. Let $F_k$ be
the generalized Hofstadter function, defined by $F_k(0) = 0$ and $F_k(m) = m - F_k^k(m - 1)$ for
$m \ge 1$, where $F_k^k$ is the $k$-fold iterate of $F_k$. Let $x_k[0]\,x_k[1] \cdots$ be the
fixed point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, and for a property $P$ of letters let $C_k^{(P)}(n)$ be the number
of indices $0 \le i < n$ with $P(x_k[i])$. Then $F_k(n) = n - C_k^{(=1)}(n)$ and
$F_k(n) = C_k^{(\ne 1)}(n)$. Moreover, $F_k(n+1) = F_k(n)$ if and only if $x_k[n] = 1$, and
$F_k(n+1) = F_k(n) + 1$ whenever $x_k[n] \ne 1$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 10 (`jis-2026-26.3.3-prop-10`).

Stated but not proved: `MetaMathlibExt.hofstadterF_eq_hofCount_ne_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-eq-hof-count-ne-one).

## The letters of $x_k$ from the increments of the iterates of $F_k$

Let $k \ge 1$, let $F_k$
be the generalized Hofstadter function with $j$-th iterate $F_k^j$ ($F_k^0$ the identity), and
let $x_k = x_k[0]\,x_k[1] \cdots$ be the fixed point of the substitution $\tau_k$
($k \mapsto k\,1$, $i \mapsto i + 1$ for $i \ne k$). For every natural number $n$: for each $j$
with $1 \le j < k$, $x_k[n] = j$ if and only if $F_k^{j-1}(n+1) = F_k^{j-1}(n) + 1$ and
$F_k^j(n+1) = F_k^j(n)$; and $x_k[n] = k$ if and only if $F_k^{k-1}(n+1) = F_k^{k-1}(n) + 1$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 11 (`jis-2026-26.3.3-prop-11`).

Stated but not proved: `MetaMathlibExt.hofWord_eq_iff_hofstadterF_iterate_diff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-word-eq-iff-hofstadter-f-iterate-dif).

## Monotonicity and asymptotics of the Hofstadter constants

For each integer $k \ge 1$ let
$\alpha_k$ be a positive zero of $X^k + X - 1$ and $\beta_k$ a positive zero of
$X^k - X^{k-1} - 1$. Then for every $k \ge 1$ we have $\alpha_k < \alpha_{k+1}$,
$\beta_{k+1} < \beta_k$, $1 + 1/k \le \beta_k \le 1 + 1/\sqrt{k}$ and
$\sqrt{k} \le \beta_k^{k-1} \le k$. Moreover $\beta_k \to 1$ and $\alpha_k \to 1$ as
$k \to \infty$, and $\alpha_k = 1 - \ln k / k + o(\ln k / k)$ and
$\beta_k = 1 + \ln k / k + o(\ln k / k)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 13 and Definition 12 (`jis-2026-26.3.3-prop-13`).

Stated but not proved: `MetaMathlibExt.hofstadter_roots_monotone_asymptotics` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-roots-monotone-asymptotics).

## Limits of Hofstadter iterates and letter frequencies

Let $k \ge 1$ and $j \ge 0$, let
$\alpha > 0$ satisfy $\alpha^k + \alpha - 1 = 0$ and let $\beta > 0$ satisfy
$\beta^k - \beta^{k-1} - 1 = 0$. Write $f^j$ for the $j$-fold iterate of a function $f$ and let
$F_k$ be the generalized Hofstadter function. Let $\tau_k$ be the substitution on letters with
$\tau_k(k) = k\,1$ and $\tau_k(i) = i + 1$ for $1 \le i < k$, let $x_k$ be the infinite word fixed
by $\tau_k$ that is the limit of the words $\tau_k^m(k)$, write $x_k[m]$ for its letter at index
$m$ (counting from $0$) and $x_k[0:n)$ for its prefix of length $n$, let
$L_k(n) = |\tau_k(x_k[0:n))|$, and for a letter $i$ let $C_k^{(=i)}(n)$ be the number of indices
$m < n$ with $x_k[m] = i$. Then, as $n \to \infty$: $F_k^j(n)/n \to \alpha^j$;
$L_k^j(n)/n \to \beta^j$; $C_k^{(=i)}(n)/n \to \alpha^{k+i-1}$ for every $i$ with $1 \le i < k$;
and $C_k^{(=k)}(n)/n \to \alpha^{k-1}$. Moreover $\alpha^{k-1} = \beta - 1$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 14 (`jis-2026-26.3.3-thm-14`).

Stated but not proved: `MetaMathlibExt.hofstadter_limits` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-limits).

## Eventual order of iterated Hofstadter functions from their growth rates

Let $k, k' \ge 1$
and $j, j' \ge 0$, let $F_k$ be the generalized Hofstadter function, write $F_k^i$ for its
$i$-fold iterate, let $\alpha > 0$ be a root of $X^k + X - 1$, and let $\alpha' > 0$ be a root of
$X^{k'} + X - 1$. If $\alpha^j < \alpha'^{j'}$, then $F_k^j(n) < F_{k'}^{j'}(n)$ for all
sufficiently large $n$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Corollary 16 (`jis-2026-26.3.3-cor-16`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_eventually_lt_of_root_pow_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-eventually-lt-of-ro).

## Eventual order of iterates of consecutive Hofstadter functions

Let $k \ge 1$, let $F_k$ be
the generalized Hofstadter function, write $F_k^i$ for its $i$-fold iterate, let $\alpha > 0$ be
a root of $X^k + X - 1$, and let $\alpha' > 0$ be a root of $X^{k+1} + X - 1$. Then for all
sufficiently large $n$, $F_k(n) < F_{k+1}(n)$, $F_{k+1}^{k+1}(n) < F_k^k(n)$ and
$F_{k+1}^{k+2}(n) < F_k^{k+1}(n)$. Moreover, for every $j \ge 0$: if $j/(j+1) \le \alpha$ or
$j^2 \le k$, then $F_{k+1}^{k+j+1}(n) < F_k^{k+j}(n)$ for all sufficiently large $n$; and if
$\alpha' \le j/(j+1)$ or $k < j$, then $F_k^{k+j}(n) < F_{k+1}^{k+j+1}(n)$ for all sufficiently
large $n$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Corollary 17 (`jis-2026-26.3.3-cor-17`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_eventual_order_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-eventual-order-succ).

## Values with exactly one preimage under a Hofstadter function

Let $k \ge 1$, let
$\alpha > 0$ satisfy $\alpha^k + \alpha - 1 = 0$ and let $\beta > 0$ satisfy
$\beta^k - \beta^{k-1} - 1 = 0$. Write $f^j$ for the $j$-fold iterate of a function $f$ and let
$F_k$ be the generalized Hofstadter function. Let $\tau_k$ be the substitution on letters with
$\tau_k(k) = k\,1$ and $\tau_k(i) = i + 1$ for $1 \le i < k$, let $x_k$ be the infinite word fixed
by $\tau_k$ that is the limit of the words $\tau_k^m(k)$, write $x_k[0:n)$ for its prefix of
length $n$ and let $L_k(n) = |\tau_k(x_k[0:n))|$. Let $U_k(n)$ be the number of $j$ with
$0 \le j < n$ for which exactly one natural number $m$ satisfies $F_k(m) = j$. Then for every
$n \ge 1$, $U_k(n) = 2n - 1 - L_k(n - 1)$ and $U_k(n) = n - F_k^{k-1}(n - 1)$. Moreover
$U_k(n)/n \to 1 - \alpha^{k-1}$ as $n \to \infty$, and $1 - \alpha^{k-1} = 2 - \beta$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 18 (`jis-2026-26.3.3-prop-18`).

Stated but not proved: `MetaMathlibExt.hofstadter_single_antecedent_count` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-single-antecedent-count).

## Order of iterates of $L_k$ against order of iterates of $F_k$

Let $F_k$ be the
generalized Hofstadter function, let $x_k[0]\,x_k[1] \cdots$ be the fixed point, beginning with
$k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every other letter $i$ to
$i + 1$, let $L_k(n)$ be the length of the word $\tau_k(x_k[0] \cdots x_k[n-1])$, and write
$f^j$ for the $j$-fold iterate of a function $f$. Let $k, k' \ge 1$ and $j, j' \ge 0$. Then
$L_k^j(n) \le L_{k'}^{j'}(n)$ for every $n$ if and only if $F_{k'}^{j'}(n) \le F_k^j(n)$ for
every $n$. Moreover, for every natural number $n$:
(a) $L_k^j(n) \le L_{k'}^{j'}(n)$ if and only if $F_{k'}^{j'}(m) \le F_k^j(m)$ for
$m = L_k^j(n)$;
(b) $L_k^j(n) < L_{k'}^{j'}(n)$ if and only if $F_{k'}^{j'}(m) < F_k^j(m)$ for
$m = L_{k'}^{j'}(n)$;
(c) if $L_k^j(m) \le L_{k'}^{j'}(m)$ for $m = F_k^j(n)$, then $F_{k'}^{j'}(n) \le F_k^j(n)$;
(d) if $F_k^j(n) < F_{k'}^{j'}(n)$, then $L_{k'}^{j'}(m) < L_k^j(m)$ for $m = F_k^j(n)$.

In (d) the paper prints $m = F_{k'}^{j'}(n)$; its proof derives (d) as the contrapositive of
(c), which gives $m = F_k^j(n)$. The printed form fails for $k = 1$, $j = 1$, $k' = 4$,
$j' = 2$ and $n = 8$: $F_1(8) = 4 < F_4^2(8) = 5$, but $L_4^2(5) = L_1(5) = 10$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 19 (`jis-2026-26.3.3-prop-19`).

Stated but not proved: `MetaMathlibExt.hofL_iterate_le_iff_hofstadterF_iterate_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-iterate-le-iff-hofstadter-f-iterat).

## Comparing $L_k$ with $L_{k+1}$

Let $x_k[0]\,x_k[1] \cdots$ be the fixed point,
beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every other
letter $i$ to $i + 1$, let $L_k(n)$ be the length of the word $\tau_k(x_k[0] \cdots x_k[n-1])$,
write $L_k^j$ for the $j$-fold iterate of $L_k$, and let $C_k^{(=k)}(n)$ be the number of
indices $i < n$ with $x_k[i] = k$. For all $k \ge 1$, $n \ge 1$ and $j$ with $0 \le j \le k$:
$L_{k+1}(n) \le L_k(n)$, $C_{k+1}^{(=k+1)}(n) \le C_k^{(=k)}(n)$, and
$L_k^j(n) < L_{k+1}^{j+1}(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 20 (`jis-2026-26.3.3-thm-20`).

Stated but not proved: `MetaMathlibExt.hofL_succ_comparison` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-succ-comparison).

## Iterates of $L_{k+1}$ lie below iterates of $L_k$

Let $x_k[0]\,x_k[1] \cdots$ be the
fixed point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, let $L_k(n)$ be the length of the word
$\tau_k(x_k[0] \cdots x_k[n-1])$, and write $L_k^j$ for the $j$-fold iterate of $L_k$. For
every $k \ge 1$, every $j \ge 0$ and every natural number $n$, $L_{k+1}^j(n) \le L_k^j(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Corollary 21 (`jis-2026-26.3.3-cor-21`).

Stated but not proved: `MetaMathlibExt.hofL_iterate_succ_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-iterate-succ-le).

## Iterates of consecutive Hofstadter functions are ordered

For every $k \ge 1$, $j \ge 0$
and $n \ge 0$, $F_k^j(n) \le F_{k+1}^j(n)$, where $F_k$ is the generalized Hofstadter function and
$F_k^j$ is its $j$-fold iterate.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 22 (`jis-2026-26.3.3-thm-22`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_le_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-le-succ).

## Shifted order of iterates of consecutive Hofstadter functions

Let $F_k$ denote the
generalized Hofstadter functions and write $f^j$ for the $j$-fold iterate of a function $f$. For
every $k \ge 1$, every $j$ with $0 \le j \le k$ and every natural number $n$,
$F_{k+1}^{j+1}(n) \le F_k^j(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Theorem 23 (`jis-2026-26.3.3-thm-23`).

Stated but not proved: `MetaMathlibExt.hofstadterF_iterate_succ_le_iterate` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hofstadter-f-iterate-succ-le-iterate).

## Comparing $L_{k+1}^{j+1}(1)$ with $L_k^j(1)$

Let $x_k[0]\,x_k[1] \cdots$ be the fixed
point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, let $L_k(n)$ be the length of the word
$\tau_k(x_k[0] \cdots x_k[n-1])$, and write $L_k^j$ for the $j$-fold iterate of $L_k$. Let
$k \ge 1$, and take differences in $\mathbb{Z}$. Then $L_{k+1}^{j+1}(1) - L_k^j(1) = 1$ for
every $j \le 2k$; $2\bigl(L_{k+1}^{j+1}(1) - L_k^j(1)\bigr) = -(j - 2k - 1)(j - 2k + 2)$ for
every $j$ with $2k \le j \le 3k$; $L_{k+1}^{2k+2}(1) = L_k^{2k+1}(1)$; and
$L_{k+1}^{j+1}(1) < L_k^j(1)$ for every $j \ge 2k + 2$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Lemma 24 (`jis-2026-26.3.3-lem-24`).

Stated but not proved: `MetaMathlibExt.hofL_iterate_one_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-iterate-one-succ-sub).

## Points where $L_k^j$ exceeds $L_{k+1}^{j+1}$

Let $x_k[0]\,x_k[1] \cdots$ be the fixed
point, beginning with $k$, of the substitution $\tau_k$ that sends $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, let $L_k(n)$ be the length of the word
$\tau_k(x_k[0] \cdots x_k[n-1])$, and write $L_k^j$ for the $j$-fold iterate of $L_k$. Let
$k \ge 1$. Then $L_{k+1}^{j+1}(2k + 3 - j) < L_k^j(2k + 3 - j)$ for every $j$ with
$k + 2 \le j \le 2k + 2$, and $L_{k+1}^{j+1}(1) < L_k^j(1)$ for every $j \ge 2k + 2$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Lemma 25 (`jis-2026-26.3.3-lem-25`).

Stated but not proved: `MetaMathlibExt.hofL_iterate_witness_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-l-iterate-witness-gt).

## Prefixes of $x_{k+1}$ contain no more letters $1$ than those of $x_k$

Let $x_k$ be the
fixed point, starting with $k$, of the substitution sending the letter $k$ to $k\,1$ and every
other letter $i$ to $i + 1$, and let $C_k^{(=1)}(n)$ be the number of indices $j < n$ with
$x_k[j] = 1$. For $k \ge 1$ and every $n \ge 0$, $C_{k+1}^{(=1)}(n) \le C_k^{(=1)}(n)$.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 26 (`jis-2026-26.3.3-prop-26`).

Stated but not proved: `MetaMathlibExt.hofCount_one_succ_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-count-one-succ-le).

## Witnesses that the letter counts of $x_k$ and $x_{k+1}$ are not ordered

For a natural
number $k$, let $\tau_k$ be the substitution sending the letter $k$ to $k\,1$ and every other
letter $a$ to $a + 1$, let $x_k = x_k[0]\,x_k[1] \cdots$ be its fixed point beginning with $k$,
let $C_k^{(=i)}(n)$ be the number of indices $j < n$ with $x_k[j] = i$, let $L_k(n)$ be the
length of the word $\tau_k(x_k[0] \cdots x_k[n-1])$, and write $L_k^j$ for the $j$-fold iterate
of $L_k$. For all natural numbers $i$ and $k$ with $3 \le i < k$, put $n = i + L_k^{2k+2}(1)$
and $m = i + L_{k+1}^{k+i}(1)$. Then $C_k^{(=i)}(n) < C_{k+1}^{(=i)}(n)$ and
$C_{k+1}^{(=i)}(m) < C_k^{(=i)}(m)$, so for these letters $i$ the letter counts of $x_k$ and
$x_{k+1}$ are not ordered.

## Sources

- Pierre Letouzey, Shuo Li, and Wolfgang Steiner, *Pointwise Order of Generalized Hofstadter Functions G, H, and Beyond*, Journal of Integer Sequences 29 (2026), Article 26.3.3, Proposition 27 (`jis-2026-26.3.3-prop-27`).

Stated but not proved: `MetaMathlibExt.hofCount_eq_witnesses` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedHofstadterOrderWanted.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html#hof-count-eq-witnesses).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Hofstadter functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/generalized-hofstadter-functions)
