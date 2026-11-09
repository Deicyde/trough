---
declaration: theorem
origin: cited
lean: Erdos1221.erdos_1221.parts.i, Erdos1221.erdos_1221.parts.ii, Erdos1221.erdos_1221.parts.iii, Erdos1221.erdos_1221.variants.r_one, Erdos1221.erdos_1221.variants.bigLambda_ge, Erdos1221.erdos_1221.variants.smallLambda_le, Erdos1221.erdos_1221.variants.mu_ge
statement: formalized
---

# Erdős Problem 1221

> *References:*
> - [erdosproblems.com/1221](https://www.erdosproblems.com/1221)
> - [dBEr49] de Bruijn, N. G. and Erdős, P., *Sequences of points on a circle*. Nederl. Akad.
>   Wetensch., Proc. (1949), 14-17 = Indagationes Math. 11 (1949), 46-49.
>   [PDF](https://www.renyi.hu/~p_erdos/1949-13.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1221.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1221](https://www.erdosproblems.com/1221).

The file states 7 research or textbook statements: 3 open and 4 solved.

## `Erdos1221.erdos_1221.parts.i`

Open: stated without proof.

> Let $a=(a_1,\ldots,a_n)$ be points, ordered consecutively, around the circle (normalised to have
> circumference $1$). Let
>
> $$M_r(a)=\max_r \lvert a_{i+r}-a_i\rvert$$
>
> and
>
> $$m_r(a)=\min_r \lvert a_{i+r}-a_i\rvert,$$
>
> where the indices are interpreted in a cyclic fashion and the distance is around the circle (in
> other words, the maximum and minimum distance between $r$-consecutive points).
>
> Let
>
> $$\Lambda_r=\inf_a \limsup_n n M_r(a_1,\ldots,a_n),$$
>
> $$\lambda_r = \sup_a \liminf_n nm_r(a_1,\ldots,a_n),$$
>
> and
>
> $$\mu_r=\inf_a \limsup_n \frac{M_r(a)}{m_r(a)},$$
>
> where the outer $\inf/\sup$ is over all infinite sequences $a=(a_1,\ldots)$.
>
> Is it true that $r(\Lambda_r-1)$, $r(1-\lambda_r)$, and $r(\mu_r-1)$ tend to infinity as
> $r\to \infty$?
>
> This is the first part, conjectured by de Bruijn and Erdős [dBEr49, §6]. We read $\Lambda_r$ and
> $\lambda_r$ as in `bigLambda` and `smallLambda`, that is, as printed. The sequences are required
> to have pairwise distinct points modulo $1$ (see `bigLambda`). Then $nM_r\geq r$ [dBEr49, §1],
> so $r(\Lambda_r-1)\to\infty$ would hold trivially. Also $m_r\geq r\,m_1$, so the sequence
> $a_k=\log_2(2k-1)$ of [dBEr49, §2] gives $\lambda_r\geq r/\log 4$, which exceeds $1$ for $r\geq2$,
> so $r(1-\lambda_r)$ would be negative for $r\geq2$. The intended conjectures are about the
> quantities normalised by $r$, so $r(\Lambda_r/r-1)=\Lambda_r-r$, and the first part asks whether
> $\Lambda_r-r\to\infty$.

```lean
theorem erdos_1221.parts.i :
    ∀ K : ℝ, ∀ᶠ r : ℕ in atTop, ENNReal.ofReal ((r : ℝ) + K) < bigLambda r
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L119).

## `Erdos1221.erdos_1221.parts.ii`

Open: stated without proof.

> Let $a=(a_1,\ldots,a_n)$ be points, ordered consecutively, around the circle (normalised to have
> circumference $1$). Let
>
> $$M_r(a)=\max_r \lvert a_{i+r}-a_i\rvert$$
>
> and
>
> $$m_r(a)=\min_r \lvert a_{i+r}-a_i\rvert,$$
>
> where the indices are interpreted in a cyclic fashion and the distance is around the circle (in
> other words, the maximum and minimum distance between $r$-consecutive points).
>
> Let
>
> $$\Lambda_r=\inf_a \limsup_n n M_r(a_1,\ldots,a_n),$$
>
> $$\lambda_r = \sup_a \liminf_n nm_r(a_1,\ldots,a_n),$$
>
> and
>
> $$\mu_r=\inf_a \limsup_n \frac{M_r(a)}{m_r(a)},$$
>
> where the outer $\inf/\sup$ is over all infinite sequences $a=(a_1,\ldots)$.
>
> Is it true that $r(\Lambda_r-1)$, $r(1-\lambda_r)$, and $r(\mu_r-1)$ tend to infinity as
> $r\to \infty$?
>
> This is the second part. As in the first part, we normalise $\lambda_r$ by $r$, so
> $r(1-\lambda_r/r)=r-\lambda_r$, and the second part asks whether $r-\lambda_r\to\infty$.

```lean
theorem erdos_1221.parts.ii :
    ∀ K : ℝ, ∀ᶠ r : ℕ in atTop, smallLambda r < ENNReal.ofReal ((r : ℝ) - K)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L146).

## `Erdos1221.erdos_1221.parts.iii`

Open: stated without proof.

> Let $a=(a_1,\ldots,a_n)$ be points, ordered consecutively, around the circle (normalised to have
> circumference $1$). Let
>
> $$M_r(a)=\max_r \lvert a_{i+r}-a_i\rvert$$
>
> and
>
> $$m_r(a)=\min_r \lvert a_{i+r}-a_i\rvert,$$
>
> where the indices are interpreted in a cyclic fashion and the distance is around the circle (in
> other words, the maximum and minimum distance between $r$-consecutive points).
>
> Let
>
> $$\Lambda_r=\inf_a \limsup_n n M_r(a_1,\ldots,a_n),$$
>
> $$\lambda_r = \sup_a \liminf_n nm_r(a_1,\ldots,a_n),$$
>
> and
>
> $$\mu_r=\inf_a \limsup_n \frac{M_r(a)}{m_r(a)},$$
>
> where the outer $\inf/\sup$ is over all infinite sequences $a=(a_1,\ldots)$.
>
> Is it true that $r(\Lambda_r-1)$, $r(1-\lambda_r)$, and $r(\mu_r-1)$ tend to infinity as
> $r\to \infty$?
>
> This is the third part. The quantity $\mu_r$ needs no normalisation, and the third part asks
> whether $r(\mu_r-1)\to\infty$, that is, whether $\mu_r>1+K/r$ for every $K$ and all large $r$.

```lean
theorem erdos_1221.parts.iii :
    ∀ K : ℝ, ∀ᶠ r : ℕ in atTop, ENNReal.ofReal (1 + K / (r : ℝ)) < mu r
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L173).

## `Erdos1221.erdos_1221.variants.r_one`

Solved: stated here without proof.

> De Bruijn and Erdős [dBEr49, §§2-5] proved that $\Lambda_1=\frac{1}{\log 2}$,
> $\lambda_1=\frac{1}{\log 4}$, and $\mu_1=2$. A sequence which witnesses this is
> $a_k=\log_2(2k-1)$. For $r=1$ the normalisation by $r$ plays no role.

```lean
theorem erdos_1221.variants.r_one :
    bigLambda 1 = ENNReal.ofReal (1 / Real.log 2) ∧
      smallLambda 1 = ENNReal.ofReal (1 / Real.log 4) ∧ mu 1 = 2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L183).

## `Erdos1221.erdos_1221.variants.bigLambda_ge`

Solved: stated here without proof.

> De Bruijn and Erdős [dBEr49, (3.3)] proved that, for any $r\geq 1$,
>
> $$\Lambda_r \geq \frac{1}{\log(1+1/r)}.$$
>
> Here $\Lambda_r$ is as in `bigLambda`, with no normalisation by $r$.

```lean
theorem erdos_1221.variants.bigLambda_ge {r : ℕ} (hr : 1 ≤ r) :
    ENNReal.ofReal (1 / Real.log (1 + 1 / (r : ℝ))) ≤ bigLambda r
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 194](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L194).

## `Erdos1221.erdos_1221.variants.smallLambda_le`

Solved: stated here without proof.

> De Bruijn and Erdős [dBEr49, (4.3)] proved that, for any $r\geq 1$,
>
> $$\lambda_r \leq \frac{r}{r+1}\frac{1}{\log(1+1/r)}.$$
>
> Here $\lambda_r$ is as in `smallLambda`, with no normalisation by $r$.

```lean
theorem erdos_1221.variants.smallLambda_le {r : ℕ} (hr : 1 ≤ r) :
    smallLambda r ≤
      ENNReal.ofReal ((r : ℝ) / ((r : ℝ) + 1) * (1 / Real.log (1 + 1 / (r : ℝ))))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 204](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L204).

## `Erdos1221.erdos_1221.variants.mu_ge`

Solved: stated here without proof.

> De Bruijn and Erdős [dBEr49, §1 and (5.7)] proved that, for any $r\geq 1$,
>
> $$\mu_r \geq 1+\frac{1}{r}.$$

```lean
theorem erdos_1221.variants.mu_ge {r : ℕ} (hr : 1 ≤ r) :
    ENNReal.ofReal (1 + 1 / (r : ℝ)) ≤ mu r
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1221.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean#L214).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1221.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1221.lean)
- [erdosproblems.com/1221](https://www.erdosproblems.com/1221)
