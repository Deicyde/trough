---
declaration: section
origin: cited
lean: MetaMathlibExt.IsBisectionSequence, MetaMathlibExt.IsBisectionSequence.le_and_le, MetaMathlibExt.IsBisectionSequence.invariants, MetaMathlibExt.IsBisectionSequence.nested, MetaMathlibExt.IsBisectionSequence.sub_eq, MetaMathlibExt.exists_isBisectionSequence, MetaMathlibExt.exists_isBisectionSequence_nested, MetaMathlibExt.bisection_nested_intervals
statement: formalized
proof: formalized
---

# Bisection method

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html).

## Bisection sequences

## Bisection sequence

For a function $f : \mathbb{R} \to \mathbb{R}$ and reals $a$, $b$, two
sequences $u, v : \mathbb{N} \to \mathbb{R}$ form a bisection sequence for $f$ from $a$ to $b$
when $u_0 = a$, $v_0 = b$, and for every $n$, writing $m_n = (u_n + v_n)/2$ for the midpoint,
either $f(m_n) \le 0$, $u_{n+1} = m_n$ and $v_{n+1} = v_n$, or $f(m_n) \ge 0$, $u_{n+1} = u_n$
and $v_{n+1} = m_n$.

These are the bracketing endpoints produced by the bisection algorithm; when $f(m_n) = 0$ either
step is allowed.

Formalized by `MetaMathlibExt.IsBisectionSequence`, a definition declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#is-bisection-sequence).

## Bisection intervals stay inside the initial interval

Let $f : \mathbb{R} \to \mathbb{R}$,
let $a \le b$, and let $u, v$ be a bisection sequence for $f$ from $a$ to $b$. Then
$a \le u_n \le v_n \le b$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsBisectionSequence.le_and_le`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#le-and-le).

## Bisection invariants

Let $f : \mathbb{R} \to \mathbb{R}$ and $a \le b$ with
$f(a) \le 0 \le f(b)$, and let $u, v$ be a bisection sequence for $f$ from $a$ to $b$. Then for
every $n \in \mathbb{N}$ we have $a \le u_n \le v_n \le b$ and $f(u_n) \le 0 \le f(v_n)$.

Formalized by `MetaMathlibExt.IsBisectionSequence.invariants`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#invariants).

## Bisection intervals are nested

Let $f : \mathbb{R} \to \mathbb{R}$, let $a \le b$, and let
$u, v$ be a bisection sequence for $f$ from $a$ to $b$. Then for every $n \in \mathbb{N}$,
$u_n \le u_{n+1} \le v_{n+1} \le v_n$.

Formalized by `MetaMathlibExt.IsBisectionSequence.nested`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#nested).

## Length of the bisection intervals

Let $f : \mathbb{R} \to \mathbb{R}$, let $a, b$ be real,
and let $u, v$ be a bisection sequence for $f$ from $a$ to $b$. Then
$v_n - u_n = (b - a)/2^n$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsBisectionSequence.sub_eq`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#sub-eq).

## Existence of bisection sequences

For every function $f : \mathbb{R} \to \mathbb{R}$ and
all reals $a$, $b$, there are sequences $u, v$ forming a bisection sequence for $f$ from $a$ to
$b$.

Formalized by `MetaMathlibExt.exists_isBisectionSequence`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#exists-is-bisection-sequence).

## Nested bisection intervals from a sign bracket

Let $f : \mathbb{R} \to \mathbb{R}$ and
$a \le b$ with $f(a) \le 0 \le f(b)$. Then there is a bisection sequence $u, v$ for $f$ from $a$
to $b$ such that for every $n \in \mathbb{N}$: $u_n \le u_{n+1} \le v_{n+1} \le v_n$,
$v_n - u_n = (b - a)/2^n$, and $f(u_n)\,f(v_n) \le 0$.

No continuity of $f$ is needed.

Formalized by `MetaMathlibExt.exists_isBisectionSequence_nested`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#exists-is-bisection-sequence-nested).

## Bisection method: nested intervals

Let $f : \mathbb{R} \to \mathbb{R}$ be continuous on
$[a, b]$, where $a \le b$ and $f(a) \le 0 \le f(b)$. Then there is a bisection sequence $u, v$
for $f$ from $a$ to $b$ such that for every $n \in \mathbb{N}$:
$u_n \le u_{n+1} \le v_{n+1} \le v_n$, $v_n - u_n = (b - a)/2^n$, and $f(u_n)\,f(v_n) \le 0$.

Proof: The endpoint pairs are defined recursively by the sign of each midpoint, and induction
proves the nesting, sign, and exact halving invariants from Burden and Faires, Section 2.1.

## Sources

- R. L. Burden and J. D. Faires, Numerical Analysis, 10th ed., Section 2.1; stable ref https://en.wikipedia.org/wiki/Bisection_method.

Formalized by `MetaMathlibExt.bisection_nested_intervals`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#bisection-nested-intervals).

## Bisection method converges at a linear rate

Let $f : \mathbb{R} \to \mathbb{R}$ be
continuous on $[a, b]$, where $a \le b$ and $f(a) \le 0 \le f(b)$, and let $u, v$ be a bisection
sequence for $f$ from $a$ to $b$. Then there is $c \in [a, b]$ with $f(c) = 0$ such that the
midpoints $(u_n + v_n)/2$ converge to $c$ and $|(u_n + v_n)/2 - c| \le (b - a)/2^{n+1}$ for
every $n \in \mathbb{N}$.

Proof: Monotone convergence gives the common endpoint limit, continuity makes it a root, and the
halved interval length gives the midpoint error bound, following Burden and Faires, Theorem 2.1.

## Sources

- R. L. Burden and J. D. Faires, Numerical Analysis, 10th ed., Theorem 2.1.

Formalized by `MetaMathlibExt.bisection_approximate_root_with_rate`, a theorem declared in [MathlibExt/Analysis/Calculus/Bisection.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Bisection.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html#bisection-approximate-root-with-rate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bisection method](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/bisection-method/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/bisection-method)
