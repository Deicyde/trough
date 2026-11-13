---
declaration: section
origin: cited
lean: MetaMathlibExt.IsWeaklyLocallyNilpotentAt, MetaMathlibExt.IsNilpotentAt, MetaMathlibExt.infinite_primes_not_dvd_mul_pow_sub, MetaMathlibExt.iterate_eval_X_add_one, MetaMathlibExt.isWeaklyLocallyNilpotentAt_X_add_one, MetaMathlibExt.not_isNilpotentAt_X_add_one, MetaMathlibExt.locallyNilpotentAt_one_classification, MetaMathlibExt.locallyNilpotentAt_neg_one_classification
statement: formalized
---

# Locally nilpotent polynomials

12 results, 5 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html).

## Weakly locally nilpotent polynomial at a point

Let $u \in \mathbb{Z}[x]$ and
$r \in \mathbb{Z}$, and let $A$ be a set of natural numbers. Write $u^{(m)}$ for the $m$-fold
iterate of $u$ as a map $\mathbb{Z} \to \mathbb{Z}$. Then $u$ is weakly locally nilpotent at $r$
outside $A$ if for every prime $p \notin A$ there is $m \ge 1$ such that $p$ divides
$u^{(m)}(r)$. For $A = \emptyset$ this is called locally nilpotent at $r$.

Only the primes in $A$ matter, so $A$ is usually taken to be a set of primes.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Section 2.

Formalized by `MetaMathlibExt.IsWeaklyLocallyNilpotentAt`, a definition declared in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#is-weakly-locally-nilpotent-at).

## Nilpotent polynomial at a point

Let $u \in \mathbb{Z}[x]$ and $r \in \mathbb{Z}$, and
write $u^{(n)}$ for the $n$-fold iterate of $u$ as a map $\mathbb{Z} \to \mathbb{Z}$. Then $u$ is
nilpotent at $r$ if $u^{(n)}(r) = 0$ for some $n \ge 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Section 2.

Formalized by `MetaMathlibExt.IsNilpotentAt`, a definition declared in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#is-nilpotent-at).

## Infinitely many primes avoid $\gamma \alpha^n - \beta$

Let $\alpha, \beta, \gamma$ be
nonzero integers such that $\beta \ne \gamma \alpha^k$ and $\beta \alpha^k \ne \gamma$ for every
natural number $k$, that is, $\beta / \gamma$ is not $\alpha^k$ for any integer $k$. Then there
are infinitely many primes $p$ such that $p$ divides none of the integers $\gamma \alpha^n - \beta$
with $n \ge 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.infinite_primes_not_dvd_mul_pow_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#infinite-primes-not-dvd-mul-pow-sub).

## Iterates of $x + 1$

Let $u(x) = x + 1 \in \mathbb{Z}[x]$ and write $u^{(m)}$ for its
$m$-fold iterate as a map $\mathbb{Z} \to \mathbb{Z}$. For every integer $r$ and every natural
number $m$, $u^{(m)}(r) = r + m$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Section 2, example (e).

Formalized by `MetaMathlibExt.iterate_eval_X_add_one`, a theorem declared in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#iterate-eval-x-add-one).

## $x + 1$ is locally nilpotent at $1$

Let $u(x) = x + 1 \in \mathbb{Z}[x]$ and write
$u^{(m)}$ for the $m$-fold iterate of $u$ as a map $\mathbb{Z} \to \mathbb{Z}$. Then for every
prime $p$ there is $m \ge 1$ such that $p$ divides $u^{(m)}(1)$.

One can take $m = p - 1$, since $u^{(p-1)}(1) = p$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Section 2, example (e).

Formalized by `MetaMathlibExt.isWeaklyLocallyNilpotentAt_X_add_one`, a theorem declared in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#is-weakly-locally-nilpotent-at-x-add-one).

## $x + 1$ is not nilpotent at $1$

The polynomial $x + 1 \in \mathbb{Z}[x]$ is not nilpotent
at $1$.

Writing $u(x) = x + 1$, the iterates satisfy $u^{(n)}(1) = n + 1 \ne 0$ for every $n \ge 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Section 2, example (e).

Formalized by `MetaMathlibExt.not_isNilpotentAt_X_add_one`, a theorem declared in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#not-is-nilpotent-at-x-add-one).

## Classification of locally nilpotent polynomials at $1$

A polynomial $u \in \mathbb{Z}[x]$
of positive degree is locally nilpotent at $1$ if and only if it has one of the following forms,
for some $p \in \mathbb{Z}[x]$: $(x-1)p(x)$ with $p \ne 0$; $-2x + 4 + p(x)(x-1)(x-2)$;
$-2x^2 + 7x - 3 + p(x)(x-1)(x-2)(x-3)$; or $u = x + 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.locallyNilpotentAt_one_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#locally-nilpotent-at-one-classification).

## Classification of locally nilpotent polynomials at $-1$

A polynomial $u \in \mathbb{Z}[x]$
of positive degree is locally nilpotent at $-1$ if and only if it has one of the following forms,
for some $p \in \mathbb{Z}[x]$: $(x+1)p(x)$ with $p \ne 0$; $-2x - 4 + p(x)(x+1)(x+2)$;
$2x^2 + 7x + 3 + p(x)(x+1)(x+2)(x+3)$; or $u = x - 1$.

These are the images of the polynomials locally nilpotent at $1$ under $u(x) \mapsto -u(-x)$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Corollary 4.2.

Stated but not proved: `MetaMathlibExt.locallyNilpotentAt_neg_one_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#locally-nilpotent-at-neg-one-classificat).

## Locally nilpotent but not nilpotent polynomials at $\pm 1$

The only polynomial
$u \in \mathbb{Z}[x]$ of positive degree that is locally nilpotent at $1$ but not nilpotent at $1$
is $x + 1$, and the only polynomial of positive degree that is locally nilpotent at $-1$ but not
nilpotent at $-1$ is $x - 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Corollary 4.3.

Stated but not proved: `MetaMathlibExt.locallyNilpotent_not_nilpotentAt_one_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#locally-nilpotent-not-nilpotent-at-one-n).

## Classification of locally nilpotent polynomials at $0$

A polynomial $u \in \mathbb{Z}[x]$
of positive degree is locally nilpotent at $0$ if and only if it has one of the following forms:
$x + b$ with $b \in \mathbb{Z}$, $b \ne 0$; $ax + b$ with $a, b \in \mathbb{Z}$, $b \ne 0$, $a$
divisible by at least one prime, and every prime divisor of $a$ dividing $b$; $x\,p(x)$ with
$p \in \mathbb{Z}[x]$, $p \ne 0$; or $(x - a)p(x)$ with $a \in \mathbb{Z}$, $a \ne 0$, and
$p \in \mathbb{Z}[x]$ with $p(0) = -1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Theorem 4.4.

Stated but not proved: `MetaMathlibExt.locallyNilpotentAt_zero_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#locally-nilpotent-at-zero-classification).

## Polynomials locally nilpotent but not nilpotent at $0$

A polynomial $u \in \mathbb{Z}[x]$
of degree at least $1$ is locally nilpotent at $0$ and not nilpotent at $0$ if and only if either
$u = x + b$ for some integer $b \ne 0$, or $u = ax + b$ for some integers $a$ and $b$ with
$b \ne 0$ such that $a$ has at least one prime divisor and every prime divisor of $a$ divides $b$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Corollary 4.5.

Stated but not proved: `MetaMathlibExt.locallyNilpotent_not_nilpotentAt_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#locally-nilpotent-not-nilpotent-at-zero).

## Linear polynomials weakly locally nilpotent but not nilpotent at $1$

Let $A$ be a finite
set of primes, and let $c$ range over the positive integers all of whose prime factors lie in $A$.
A polynomial $u \in \mathbb{Z}[x]$ of degree $1$ is weakly locally nilpotent at $1$ outside $A$ and
not nilpotent at $1$ if and only if $u$ is one of: $x + c$; $x - c$ with $c \ne 1$; $cx + 1$ or
$-cx + 1$ with $c \ne 1$; or $-2x - 1$, the last only when $2 \in A$.

Writing $c = q_1^{s_1} \cdots q_k^{s_k}$ with the $q_i$ the primes of $A$, the condition $c \ne 1$
is the paper's $\sum s_i \ge 1$.

## Sources

- Sayak Sengupta, *Locally Nilpotent Polynomials over Z*, INTEGERS 24 (2024), Article A13, Corollary 5.2.

Stated but not proved: `MetaMathlibExt.linear_weaklyLocallyNilpotent_not_nilpotentAt_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocallyNilpotentPolynomialsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html#linear-weakly-locally-nilpotent-not-nilp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Locally nilpotent polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/locally-nilpotent-polynomials)
