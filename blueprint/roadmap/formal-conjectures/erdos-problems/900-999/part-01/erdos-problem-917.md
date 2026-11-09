---
declaration: theorem
origin: cited
lean: Erdos917.erdos_917.parts.i, Erdos917.erdos_917.parts.ii, Erdos917.erdos_917.parts.iii, Erdos917.erdos_917.variants.lower_construction, Erdos917.erdos_917.variants.not_asymptotic, Erdos917.erdos_917.variants.three_dvd, Erdos917.erdos_917.variants.dirac, Erdos917.erdos_917.variants.erdos_three_dvd, Erdos917.erdos_917.variants.stiebitz_upper, Erdos917.erdos_917.variants.luo_ma_yang
statement: formalized
---

# Erdős Problem 917

> *References:*
> - [erdosproblems.com/917](https://www.erdosproblems.com/917)
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
>   [PDF](https://www.renyi.hu/~p_erdos/1969-13.pdf)
> - [Er93] Erdős, P., *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. 16 (1993), 333-350.
> - [Di52] Dirac, G. A., *A property of $4$-chromatic graphs and some remarks on critical graphs*.
>   J. London Math. Soc. 27 (1952), 85-92.
> - [To70] Toft, B., *On the maximal number of edges of critical $k$-chromatic graphs*. Studia Sci.
>   Math. Hungar. 5 (1970), 461-470.
> - [St87] Stiebitz, M., *Subgraphs of colour-critical graphs*. Combinatorica 7 (1987), 303-312.
> - [LMY23] Luo, C., Ma, J. and Yang, T., *On the maximum number of edges in $k$-critical graphs*.
>   Combin. Probab. Comput. 32 (2023), 900-911.
>   [arXiv:2301.01656](https://arxiv.org/abs/2301.01656)
>
> The question is due to Erdős [Er69b, p. 28]; see also [Er93, p. 341]. See also
> [erdosproblems.com/944](https://www.erdosproblems.com/944) and
> [erdosproblems.com/1032](https://www.erdosproblems.com/1032).

*Quoted from [FormalConjectures/ErdosProblems/917.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/917](https://www.erdosproblems.com/917).

The file states 10 research or textbook statements: 2 open and 8 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos917.erdos_917.parts.i`

Solved: stated here without proof.

> Let $k\geq 4$ and $f_k(n)$ be the largest number of edges in a graph on $n$ vertices which has
> chromatic number $k$ and is critical (i.e. deleting any edge reduces the chromatic number).
>
> Is it true that
> $$f_k(n) \gg_k n^2?$$
>
> This is the first part. It was proved by Toft [To70]. We read $\gg_k$ as: for each $k$ there is
> $c > 0$ with $f_k(n) \geq cn^2$ for all large $n$.

```lean
theorem erdos_917.parts.i :
    ∀ k : ℕ, 4 ≤ k → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, c * (n : ℝ) ^ 2 ≤ (f k n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L105).

## `Erdos917.erdos_917.parts.ii`

Open: stated without proof.

> Let $k\geq 4$ and $f_k(n)$ be the largest number of edges in a graph on $n$ vertices which has
> chromatic number $k$ and is critical (i.e. deleting any edge reduces the chromatic number).
>
> Is it true that
> $$f_6(n)\sim n^2/4?$$
>
> This is the second part.

```lean
theorem erdos_917.parts.ii :
    (fun n : ℕ ↦ (f 6 n : ℝ)) ~[atTop] (fun n : ℕ ↦ (n : ℝ) ^ 2 / 4)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L119).

## `Erdos917.erdos_917.parts.iii`

Solved: stated here without proof.

> Let $k\geq 4$ and $f_k(n)$ be the largest number of edges in a graph on $n$ vertices which has
> chromatic number $k$ and is critical (i.e. deleting any edge reduces the chromatic number).
>
> More generally, is it true that, for $k\geq 6$,
> $$f_k(n) \sim \frac{1}{2}\left(1-\frac{1}{\lfloor k/3\rfloor}\right)n^2?$$
>
> This is the third part. It has a negative answer: the constructions in
> `erdos_917.variants.lower_construction` disprove it for $k \not\equiv 0 \pmod 3$
> (see `erdos_917.variants.not_asymptotic`).

```lean
theorem erdos_917.parts.iii :
    ¬ ∀ k : ℕ, 6 ≤ k → (fun n : ℕ ↦ (f k n : ℝ)) ~[atTop] conjecturedValue k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L135).

## `Erdos917.erdos_917.variants.lower_construction`

Solved: stated here without proof.

> Constructions of Stiebitz [St87] show that, for $k\geq 6$, there exist infinitely many values of
> $n$ such that
> $$f_k(n) \geq \frac{1}{2}\left(1-\frac{1}{\lfloor k/3\rfloor+\delta_k}\right)n^2$$
> where $\delta_k=0$ if $k\equiv 0\pmod{3}$, $\delta_k=1/7$ if $k\equiv 1\pmod{3}$, and
> $\delta_k = 24/69$ if $k\equiv 2\pmod{3}$.
>
> [LMY23] state the same bound in the form $(\frac12-\frac{3}{2k-\delta_k'})n^2$ with
> $\delta_k'=0,8/7,44/23$, and credit the constructions to Toft [To70].

```lean
theorem erdos_917.variants.lower_construction (k : ℕ) (hk : 6 ≤ k) :
    ∃ᶠ n : ℕ in atTop,
      1 / 2 * (1 - 1 / (((k / 3 : ℕ) : ℝ) + delta k)) * (n : ℝ) ^ 2 ≤ (f k n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L150).

## `Erdos917.erdos_917.variants.not_asymptotic`

Solved: stated here without proof.

> The constructions in `erdos_917.variants.lower_construction` disprove Erdős' conjectured asymptotic
> $f_k(n) \sim \frac{1}{2}\left(1-\frac{1}{\lfloor k/3\rfloor}\right)n^2$ for $k\not\equiv 0\pmod{3}$,
> $k \geq 6$.

```lean
theorem erdos_917.variants.not_asymptotic (k : ℕ) (hk : 6 ≤ k) (h3 : ¬ 3 ∣ k) :
    ¬ (fun n : ℕ ↦ (f k n : ℝ)) ~[atTop] conjecturedValue k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L161).

## `Erdos917.erdos_917.variants.three_dvd`

Open: stated without proof.

> The remaining case of the third question: is it true that, for $k\geq 6$ with $3 \mid k$,
> $$f_k(n) \sim \frac{1}{2}\left(1-\frac{1}{\lfloor k/3\rfloor}\right)n^2?$$
> For $k = 6$ this is `erdos_917.parts.ii`.

```lean
theorem erdos_917.variants.three_dvd :
    ∀ k : ℕ, 6 ≤ k → 3 ∣ k → (fun n : ℕ ↦ (f k n : ℝ)) ~[atTop] conjecturedValue k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L171).

## `Erdos917.erdos_917.variants.dirac`

Solved: stated here without proof.

> In fact Dirac [Di52] proved
> $$f_6(4n+2) \geq 4n^2+8n+3,$$
> as witnessed by taking two disjoint copies of $C_{2n+1}$ and adding all edges between them.
>
> We take $n \geq 1$, so that $C_{2n+1}$ is a cycle.

```lean
theorem erdos_917.variants.dirac (n : ℕ) (hn : 1 ≤ n) :
    4 * n ^ 2 + 8 * n + 3 ≤ f 6 (4 * n + 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L183).

## `Erdos917.erdos_917.variants.erdos_three_dvd`

Solved: stated here without proof.

> Erdős [Er69b] observed that Dirac's construction generalises to show that, if $3\mid k$, there are
> infinitely many values of $n$ (those of the shape $mk/3$ where $m$ is odd) such that
> $$f_k(n) \geq \frac{1}{2}\left(1-\frac{1}{k/3}\right)n^2 + n.$$
>
> We take $m \geq 3$, so that the cycle $C_m$ exists.

```lean
theorem erdos_917.variants.erdos_three_dvd (k : ℕ) (hk : 3 ≤ k) (h3 : 3 ∣ k) (m : ℕ)
    (hm : Odd m) (hm3 : 3 ≤ m) :
    conjecturedValue k (m * (k / 3)) + ((m * (k / 3) : ℕ) : ℝ) ≤ (f k (m * (k / 3)) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L195).

## `Erdos917.erdos_917.variants.stiebitz_upper`

Solved: stated here without proof.

> Stiebitz also proved the general upper bound
> $$f_k(n) < \mathrm{ex}(n;K_{k-1})\sim \frac{1}{2}\left(1-\frac{1}{k-2}\right)n^2$$
> for large $n$.
>
> Here $k \geq 4$, as in [LMY23].

```lean
theorem erdos_917.variants.stiebitz_upper (k : ℕ) (hk : 4 ≤ k) :
    ∀ᶠ n : ℕ in atTop,
      f k n < SimpleGraph.extremalNumber n (SimpleGraph.completeGraph (Fin (k - 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 208](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L208).

## `Erdos917.erdos_917.variants.luo_ma_yang`

Solved: stated here without proof.

> Luo, Ma, and Yang [LMY23] have improved this upper bound to
> $$f_k(n) \leq \frac{1}{2}\left(1-\frac{1}{k-2}-\frac{1}{36(k-1)^2}+o(1)\right)n^2.$$
>
> [LMY23, Theorem 1.1] proves the stronger bound
> $f_k(n) \leq \mathrm{ex}(n;K_{k-1}) - \frac{n^2}{36(k-1)^2}$ for $k \geq 4$ and all large $n$, where
> $\mathrm{ex}(n;K_{k-1})$ is the number of edges of the Turán graph $T_{k-2}(n)$. We state this form.

```lean
theorem erdos_917.variants.luo_ma_yang (k : ℕ) (hk : 4 ≤ k) :
    ∀ᶠ n : ℕ in atTop, (f k n : ℝ) ≤
      (SimpleGraph.extremalNumber n (SimpleGraph.completeGraph (Fin (k - 1))) : ℝ) -
        (n : ℝ) ^ 2 / (36 * ((k : ℝ) - 1) ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/917.lean, line 222](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean#L222).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/917.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/917.lean)
- [erdosproblems.com/917](https://www.erdosproblems.com/917)
