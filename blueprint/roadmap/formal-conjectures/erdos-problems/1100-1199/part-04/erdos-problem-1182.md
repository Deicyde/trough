---
declaration: theorem
origin: cited
lean: Erdos1182.erdos_1182.parts.i, Erdos1182.erdos_1182.parts.ii, Erdos1182.erdos_1182.parts.iii, Erdos1182.erdos_1182.variants.ramsey_ge, Erdos1182.erdos_1182.variants.chvatal, Erdos1182.erdos_1182.variants.F_ge_pred, Erdos1182.erdos_1182.variants.befrs_lower, Erdos1182.erdos_1182.variants.befrs_upper, Erdos1182.erdos_1182.variants.brandt, Erdos1182.erdos_1182.variants.nikiforov_rousseau, Erdos1182.erdos_1182.variants.brandt_expects, Erdos1182.erdos_1182.variants.f_lower, Erdos1182.erdos_1182.variants.f_upper, Erdos1182.erdos_1182.variants.small_values
statement: formalized
---

# Erdős Problem 1182

> *References:*
> - [erdosproblems.com/1182](https://www.erdosproblems.com/1182)
> - [Er78] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
>   [PDF](https://www.renyi.hu/~p_erdos/1978-36.pdf)
> - [BEFRS80] Burr, S. A., Erdős, P., Faudree, R. J., Rousseau, C. C. and Schelp, R. H., *An extremal
>   problem in generalized Ramsey theory*. Ars Combin. 10 (1980), 193-203.
>   [PDF](https://www.renyi.hu/~p_erdos/1980-04.pdf)
> - [Br96] Brandt, S., *Expanding graphs and Ramsey numbers*. Freie Universität Berlin, preprint
>   A 96-24 (1996).
> - [BBH98] Brandt, S., Brinkmann, G. and Harmuth, T., *All Ramsey numbers $r(K_3,G)$ for connected
>   graphs of order 9*. Electron. J. Combin. 5 (1998), #R7.
> - [Ch77] Chvátal, V., *Tree-complete graph Ramsey numbers*. J. Graph Theory 1 (1977), 93.
> - [NiRo09] Nikiforov, V. and Rousseau, C. C., *Ramsey goodness and beyond*. Combinatorica 29
>   (2009), 227-262.

*Quoted from [FormalConjectures/ErdosProblems/1182.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1182](https://www.erdosproblems.com/1182).

The file states 14 research or textbook statements: 2 open, 11 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos1182.erdos_1182.parts.i`

Open: stated without proof.

> Let $f(n)$ be maximal such that there is a connected graph $G$ with $n$ vertices and $f(n)$ edges
> such that
>
> $$R(K_3,G)= 2n-1.$$
>
> Let $F(n)$ be maximal such that every connected graph $G$ with $n$ vertices and $\leq F(n)$ edges
> has
>
> $$R(K_3,G)= 2n-1.$$
>
> Estimate $f(n)$ and $F(n)$. In particular, is it true that $F(n)/n\to \infty$?
>
> This is the first part: estimate $f(n)$. The problem is due to Burr, Erdős, Faudree, Rousseau and
> Schelp [BEFRS80] and appears in [Er78, p. 33]. We read "estimate" as the order of magnitude
> `=Θ`. Burr, Erdős, Faudree, Rousseau and Schelp [BEFRS80, Theorem 2] proved
> $n^{3/2}(\log n)^{1/2}\ll f(n)\ll n^{5/3}(\log n)^{2/3}$ (`erdos_1182.variants.f_lower`,
> `erdos_1182.variants.f_upper`).

```lean
theorem erdos_1182.parts.i :
    (fun n : ℕ ↦ (f n : ℝ)) =Θ[atTop] erdos_1182.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L108).

## `Erdos1182.erdos_1182.parts.ii`

Solved: stated here without proof.

> Let $f(n)$ be maximal such that there is a connected graph $G$ with $n$ vertices and $f(n)$ edges
> such that
>
> $$R(K_3,G)= 2n-1.$$
>
> Let $F(n)$ be maximal such that every connected graph $G$ with $n$ vertices and $\leq F(n)$ edges
> has
>
> $$R(K_3,G)= 2n-1.$$
>
> Estimate $f(n)$ and $F(n)$. In particular, is it true that $F(n)/n\to \infty$?
>
> This is the second part: estimate $F(n)$. As an order of magnitude, `=Θ`, this is known:
> $F(n)=\Theta(n)$, by $F(n)\ge n-1$ (`erdos_1182.variants.F_ge_pred`, from Chvátal's theorem
> [Ch77]) and the linear upper bounds of `erdos_1182.variants.brandt` and
> `erdos_1182.variants.nikiforov_rousseau`. The finer question of the asymptotic behaviour of
> $F(n)/n$ is open, see `erdos_1182.variants.brandt_expects`.

```lean
theorem erdos_1182.parts.ii :
    (fun n : ℕ ↦ (F n : ℝ)) =Θ[atTop] erdos_1182.parts.ii.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L130).

## `Erdos1182.erdos_1182.parts.iii`

Solved: stated here without proof.

> Let $f(n)$ be maximal such that there is a connected graph $G$ with $n$ vertices and $f(n)$ edges
> such that
>
> $$R(K_3,G)= 2n-1.$$
>
> Let $F(n)$ be maximal such that every connected graph $G$ with $n$ vertices and $\leq F(n)$ edges
> has
>
> $$R(K_3,G)= 2n-1.$$
>
> Estimate $f(n)$ and $F(n)$. In particular, is it true that $F(n)/n\to \infty$?
>
> This is the third part, asked in [BEFRS80, Section 5] and in [Er78, pp. 33-34], where Erdős says
> it seems certain. The answer is no: Brandt [Br96] proved $F(n)\le 84n$ (as recorded on the problem
> page, see `erdos_1182.variants.brandt`), and [NiRo09, Theorem 5.1] implies $F(n)<50n$ for large
> $n$ (see `erdos_1182.variants.nikiforov_rousseau`).

```lean
theorem erdos_1182.parts.iii :
    ¬ Tendsto (fun n : ℕ ↦ (F n : ℝ) / n) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L149).

## `Erdos1182.erdos_1182.variants.ramsey_ge`

Textbook result, stated without proof.

> It is trivial that $R(K_3,G)\geq 2n-1$ for any connected graph $G$ on $n$ vertices
> ([BEFRS80, p. 193]).

```lean
theorem erdos_1182.variants.ramsey_ge {n : ℕ} (G : SimpleGraph (Fin n)) (hG : G.Connected) :
    2 * n - 1 ≤ SimpleGraph.graphRamsey (⊤ : SimpleGraph (Fin 3)) G
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L158).

## `Erdos1182.erdos_1182.variants.chvatal`

Solved: stated here without proof.

> By a result of Chvátal [Ch77], $R(K_3,T)=2n-1$ whenever $T$ is a tree on $n$ vertices (as stated
> in [BEFRS80, p. 193]).

```lean
theorem erdos_1182.variants.chvatal {n : ℕ} (T : SimpleGraph (Fin n)) (hT : T.IsTree) :
    IsTriangleGood T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 167](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L167).

## `Erdos1182.erdos_1182.variants.F_ge_pred`

Solved: stated here without proof.

> Every connected graph with at most $n-1$ edges is a tree, so Chvátal's theorem [Ch77] gives
> $F(n)\geq n-1$ ([BEFRS80, p. 193]).

```lean
theorem erdos_1182.variants.F_ge_pred {n : ℕ} (hn : 2 ≤ n) : n - 1 ≤ F n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L176).

## `Erdos1182.erdos_1182.variants.befrs_lower`

Solved: stated here without proof.

> Burr, Erdős, Faudree, Rousseau and Schelp [BEFRS80, Theorem 1(a)] proved
>
> $$\frac{17n+1}{15}\leq F(n),$$
>
> the lower bound for all $n\geq 4$.
>
> We state the integer-part version $n+\lfloor (2n+1)/15\rfloor\le F(n)$, which is what the proof
> gives (the number $k$ of extra edges there is an integer with $0\le k\le (2n+1)/15$) and which
> follows from the printed bound because $n+\lfloor (2n+1)/15\rfloor\leq(17n+1)/15$.

```lean
theorem erdos_1182.variants.befrs_lower {n : ℕ} (hn : 4 ≤ n) :
    n + (2 * n + 1) / 15 ≤ F n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L189).

## `Erdos1182.erdos_1182.variants.befrs_upper`

Solved: stated here without proof.

> Burr, Erdős, Faudree, Rousseau and Schelp [BEFRS80, Theorem 1(b)] proved
>
> $$F(n)\leq \left(\frac{27}{4}+o(1)\right)n(\log n)^2.$$
>
> This is superseded by the linear bounds of `erdos_1182.variants.brandt` and
> `erdos_1182.variants.nikiforov_rousseau`.

```lean
theorem erdos_1182.variants.befrs_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (F n : ℝ) < (27 / 4 + ε) * n * Real.log n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L200).

## `Erdos1182.erdos_1182.variants.brandt`

Solved: stated here without proof.

> The upper bound was improved to $F(n)\leq 84n$ by Brandt [Br96]. (This resolves the final
> question in the negative.)
>
> We have not seen the preprint [Br96]; the bound is as recorded on the problem page, and we state
> it for all large $n$. Brandt's method uses expander graphs: almost all regular graphs of large
> degree are not $3$-good. In [BBH98, p. 6], of which Brandt is a coauthor, it is stated without
> proof that it gives $F(n)<12n$ for large $n$ (there $F(n)$ is called $f(K_3,n)$).

```lean
theorem erdos_1182.variants.brandt :
    ∀ᶠ n : ℕ in atTop, F n ≤ 84 * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L214).

## `Erdos1182.erdos_1182.variants.nikiforov_rousseau`

Solved: stated here without proof.

> Nikiforov and Rousseau [NiRo09, Theorem 5.1] proved that for $n$ sufficiently large almost all
> connected $100$-regular graphs of order $n$ are not $3$-good. Such a graph has $50n$ edges (and
> connected $100$-regular graphs of order $n$ exist for all $n\geq 101$), so $F(n)<50n$ for all
> large $n$. This gives a proved linear upper bound for $F$, answering the third part.

```lean
theorem erdos_1182.variants.nikiforov_rousseau :
    ∀ᶠ n : ℕ in atTop, F n < 50 * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 225](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L225).

## `Erdos1182.erdos_1182.variants.brandt_expects`

Open: stated without proof.

> Brandt [Br96] expects that for all large $n$ we have $2n\lt F(n)<6n$ (as recorded on the problem
> page).

```lean
theorem erdos_1182.variants.brandt_expects :
    ∀ᶠ n : ℕ in atTop, 2 * n < F n ∧ F n < 6 * n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 234](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L234).

## `Erdos1182.erdos_1182.variants.f_lower`

Solved: stated here without proof.

> Burr, Erdős, Faudree, Rousseau and Schelp [BEFRS80, Theorem 2] proved that there is a constant
> $A>0$ with
>
> $$n^{3/2}(\log n)^{1/2} \ll f(n),$$
>
> more precisely $An^{3/2}(\log n)^{1/2}\lt f(n)$ for all sufficiently large $n$.

```lean
theorem erdos_1182.variants.f_lower :
    ∃ A > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      A * (n : ℝ) ^ (3 / 2 : ℝ) * Real.sqrt (Real.log n) < (f n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 245](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L245).

## `Erdos1182.erdos_1182.variants.f_upper`

Solved: stated here without proof.

> Burr, Erdős, Faudree, Rousseau and Schelp [BEFRS80, Theorem 2] proved that there is a constant
> $B>0$ with
>
> $$f(n)\ll n^{5/3}(\log n)^{2/3},$$
>
> more precisely $f(n)\lt Bn^{5/3}(\log n)^{2/3}$ for all sufficiently large $n$.

```lean
theorem erdos_1182.variants.f_upper :
    ∃ B > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (f n : ℝ) < B * (n : ℝ) ^ (5 / 3 : ℝ) * Real.log n ^ (2 / 3 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 257](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L257).

## `Erdos1182.erdos_1182.variants.small_values`

Solved: stated here without proof.

> The first few values of $F(n)$ and $f(n)$ (beginning with $n=2$) are $1,2,5,7,8$ and $1,2,5,8,12$
> respectively, as reported in [BEFRS80, Table I]. Brandt, Brinkmann and Harmuth [BBH98, Table 2]
> extended these (by computer) to all $n\le 12$:
>
> $$F(n):\ 1,2,5,7,8,11,11,16,18,23,23,\qquad f(n):\ 1,2,5,8,12,16,20,27,33,41,49$$
>
> for $n=2,\ldots,12$. (The value for $n=2$ is from [BEFRS80]; [BBH98] start at $n=3$.)

```lean
theorem erdos_1182.variants.small_values :
    (F 2 = 1 ∧ F 3 = 2 ∧ F 4 = 5 ∧ F 5 = 7 ∧ F 6 = 8 ∧ F 7 = 11 ∧ F 8 = 11 ∧ F 9 = 16 ∧
      F 10 = 18 ∧ F 11 = 23 ∧ F 12 = 23) ∧
    (f 2 = 1 ∧ f 3 = 2 ∧ f 4 = 5 ∧ f 5 = 8 ∧ f 6 = 12 ∧ f 7 = 16 ∧ f 8 = 20 ∧ f 9 = 27 ∧
      f 10 = 33 ∧ f 11 = 41 ∧ f 12 = 49)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1182.lean, line 270](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean#L270).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1182.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1182.lean)
- [erdosproblems.com/1182](https://www.erdosproblems.com/1182)
