---
declaration: theorem
origin: cited
lean: Erdos1001.erdos_1001.parts.i, Erdos1001.erdos_1001.variants.est_formula
statement: formalized
---

# Erdős Problem 1001

> *References:*
> - [erdosproblems.com/1001](https://www.erdosproblems.com/1001)
> - [Er64b] Erdős, P., *Problems and results on diophantine approximations*. Compositio Math.
>   16 (1964), 52-65. [PDF](https://www.numdam.org/item/CM_1964__16__52_0.pdf)
> - [EST58] Erdős, P. and Szüsz, P. and Turán, P., *Remarks on the theory of diophantine
>   approximation*. Colloq. Math. 6 (1958), 119-126.
> - [KeSo66] Kesten, H. and Sós, V. T., *On two problems of Erdős, Szüsz and Turán concerning
>   diophantine approximations*. Acta Arith. 12 (1966/67), 183-192.
> - [XiZa06] Xiong, Maosheng and Zaharescu, Alexandru, *A problem of Erdős-Szüsz-Turán on
>   diophantine approximation*. Acta Arith. 125 (2006), 163-177.
> - [Bo08] Boca, Florin P., *A problem of Erdős, Szüsz and Turán concerning Diophantine
>   approximations*. Int. J. Number Theory 4 (2008), 691-708.

*Quoted from [FormalConjectures/ErdosProblems/1001.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1001.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1001](https://www.erdosproblems.com/1001).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1001.erdos_1001.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1001.lean#L8077](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1001.lean#L8077).

> Let $S(N,A,c)$ be the measure of the set of those $\alpha\in (0,1)$ such that
> $$\left\lvert \alpha-\frac{x}{y}\right\rvert< \frac{A}{y^2}$$
> for some $N\leq y\leq cN$ and $(x,y)=1$. Does
> $$\lim_{N\to \infty}S(N,A,c)=f(A,c)$$
> exist?
>
> This is a problem of Erdős, Szüsz, and Turán [EST58], restated in [Er64b, p. 62]. The existence
> of the limit for all $A>0$ and $c\geq 1$ was proved by Kesten and Sós [KeSo66]. Boca [Bo08] and
> Xiong and Zaharescu [XiZa06, Theorem 2] gave further proofs. We assume $A>0$ and $c\geq 1$,
> since otherwise $S=0$. The second question, the explicit form of $f(A,c)$, is not stated here.

```lean
theorem erdos_1001.parts.i (A c : ℝ) (hA : 0 < A) (hc : 1 ≤ c) :
    ∃ f : ℝ, Tendsto (fun N : ℕ ↦ S N A c) atTop (𝓝 f)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1001.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1001.lean#L76).

## `Erdos1001.erdos_1001.variants.est_formula`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1001.lean#L1047](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1001.lean#L1047).

> Erdős, Szüsz, and Turán [EST58] proved that
> $$f(A,c)=\frac{12 A\log c}{\pi^2}$$
> when $0\lt A< \frac{c}{1+c^2}$. Here $c\geq 1$, since the range $N\leq y\leq cN$ is empty for
> $c<1$.

```lean
theorem erdos_1001.variants.est_formula (A c : ℝ) (hA : 0 < A) (hc : 1 ≤ c)
    (hAc : A < c / (1 + c ^ 2)) :
    Tendsto (fun N : ℕ ↦ S N A c) atTop (𝓝 (12 * A * Real.log c / Real.pi ^ 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1001.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1001.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1001.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1001.lean)
- [erdosproblems.com/1001](https://www.erdosproblems.com/1001)
