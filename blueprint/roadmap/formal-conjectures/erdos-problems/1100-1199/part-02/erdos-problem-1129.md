---
declaration: theorem
origin: cited
lean: Erdos1129.erdos_1129, Erdos1129.erdos_1129.variants.canonical, Erdos1129.erdos_1129.variants.unique, Erdos1129.erdos_1129.variants.free_nodes_not_unique, Erdos1129.erdos_1129.variants.three_nodes, Erdos1129.erdos_1129.variants.four_nodes, Erdos1129.erdos_1129.variants.erdos_lower_bound, Erdos1129.erdos_1129.variants.chebyshev_upper_bound
statement: formalized
---

# Erdős Problem 1129

> *References:*
> - [erdosproblems.com/1129](https://www.erdosproblems.com/1129)
> - [Be31] Bernstein, S., *Sur la limitation des valeurs d'un polynôme P_n(x) de degré n sur
>   tout un segment par ses valeurs en (n+1) points du segment*. Izv. Akad. Nauk SSSR 7 (1931),
>   1025-1050.
> - [dBPi78] de Boor, C. and Pinkus, A., *Proof of the conjectures of Bernstein and Erdős
>   concerning the optimal nodes for polynomial interpolation*. J. Approx. Theory 24 (1978),
>   289-303.
> - [Er47] Erdős, P., *Some remarks on polynomials*. Bull. Amer. Math. Soc. 53 (1947), 1169-1176.
>   [PDF](https://www.renyi.hu/~p_erdos/1947-08.pdf)
> - [Er61c] Erdős, P., *Problems and results on the theory of interpolation. II*. Acta Math.
>   Acad. Sci. Hungar. 12 (1961), 235-244. [PDF](https://www.renyi.hu/~p_erdos/1961-20.pdf)
> - [Er67] Erdős, P., *Problems and results on the convergence and divergence properties of the
>   Lagrange interpolation polynomials and some extremal problems*. Mathematica (Cluj) (1967),
>   65-73. [PDF](https://www.renyi.hu/~p_erdos/1967-20.pdf)
> - [Fa14] Faber, G., *Über die interpolatorische Darstellung stetiger Funktionen*. Jahresber.
>   Deutsch. Math.-Verein. 23 (1914), 190-210.
> - [Ib16] Ibrahimoglu, B. A., *Lebesgue functions and Lebesgue constants in polynomial
>   interpolation*. J. Inequal. Appl. (2016), Paper No. 93.
>   [DOI](https://doi.org/10.1186/s13660-016-1030-3)
> - [Ki77] Kilgore, T. A., *Optimization of the norm of the Lagrange interpolation operator*.
>   Bull. Amer. Math. Soc. 83 (1977), 1069-1071.
> - [Ki78] Kilgore, T. A., *A characterization of the Lagrange interpolating projection with
>   minimal Tchebycheff norm*. J. Approx. Theory 24 (1978), 273-288.
> - [RaVa15] Rack, H.-J. and Vajda, R., *Optimal cubic Lagrange interpolation: Extremal node
>   systems with minimal Lebesgue constant*. Stud. Univ. Babeş-Bolyai Math. 60 (2015), 151-171.
>   [Link](https://studia.reviste.ubbcluj.ro/index.php/subbmathematica/article/view/5710)
> - [Ren26] Ren, C. Y., *Erdős 1129: all optimal free interpolation nodes*, Lean formalisation
>   (2026), building on randyxian08's Lean formalisation of the canonical case.
>   [GitHub](https://github.com/CollinYuanjieRen/awards/blob/791bf61df4366b60b6b47b9e062661ee65b3143b/submissions/jsp-000936-cyr/README.md)
>
> See also [erdosproblems.com/1130](https://www.erdosproblems.com/1130), which uses the
> definitions of this file.

*Quoted from [FormalConjectures/ErdosProblems/1129.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1129](https://www.erdosproblems.com/1129).

The file states 8 research or textbook statements: 8 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1129.erdos_1129`

Solved: stated here without proof.

> For $x_1,\ldots,x_n\in [-1,1]$ let
>
> $$l_k(x)=\frac{\prod_{i\neq k}(x-x_i)}{\prod_{i\neq k}(x_k-x_i)},$$
>
> which are such that $l_k(x_k)=1$ and $l_k(x_i)=0$ for $i\neq k$.
>
> Describe which choice of $x_i$ minimise
>
> $$\Lambda(x_1,\ldots,x_n)=\max_{x\in [-1,1]} \sum_k \lvert l_k(x)\rvert.$$
>
> A problem of Bernstein [Be31] and Erdős [Er47, p. 1171], [Er67, p. 66]. They conjectured that
> the minimisers are characterised by equioscillation of the Lebesgue function. This was proved by
> Kilgore [Ki77], [Ki78] and by de Boor and Pinkus [dBPi78] for canonical node sets, that is, node
> sets with $x_1=-1$ and $x_n=1$ (see [Ib16, Section 3.7] and [RaVa15, Proposition 2.8]); this is
> `erdos_1129.variants.canonical`.
>
> Here the minimisers range over all node sets in $[-1,1]$, as in the question. For $n\ge 3$ there
> are uncountably many of them [RaVa15, Theorem 2.5] (`erdos_1129.variants.free_nodes_not_unique`):
> suitable affine images of the canonical minimiser inside $[-1,1]$ are minimisers too. All of them
> are described in the Lean formalisation [Ren26], which erdosproblems.com lists for this problem:
> for $n\ge 2$ a node set minimises $\Lambda$ if and only if its local maxima between consecutive
> nodes are all equal and both $\sum_k\lvert l_k(-1)\rvert$ and $\sum_k\lvert l_k(1)\rvert$ are at
> most that common value, and for $n=1$ every node set minimises $\Lambda$. For $n=4$ all minimisers
> are also given in [RaVa15, Theorem 5.2].

```lean
theorem erdos_1129 (n : ℕ) :
    {x : Fin n → ℝ | IsMinimiser x} = erdos_1129.answer n
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L155).

## `Erdos1129.erdos_1129.variants.canonical`

Solved: stated here without proof.

> The theorem of Kilgore [Ki77], [Ki78] and de Boor and Pinkus [dBPi78] for canonical node sets
> ($x_1=-1$, $x_n=1$), as in [Ib16, Section 3.7] and [RaVa15, Definition 2.7 and Proposition 2.8]:
> the canonical node sets that minimise $\Lambda$ among all node sets are exactly the canonical node
> sets whose local maxima $\lambda_i=\max_{[x_i,x_{i+1}]}\sum_k\lvert l_k\rvert$ between consecutive
> nodes are all equal. The two outer gaps $[-1,x_1]$ and $[x_n,1]$ are single points for canonical
> nodes and are not used.

```lean
theorem erdos_1129.variants.canonical (n : ℕ) :
    {x : Fin n → ℝ | IsCanonical x ∧ IsMinimiser x} = {x | IsCanonical x ∧ Equioscillates x}
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L168).

## `Erdos1129.erdos_1129.variants.unique`

Solved: stated here without proof.

> Kilgore [Ki78] and de Boor and Pinkus [dBPi78] proved that for $n\ge 2$ there is at most one
> canonical node set whose local maxima $\lambda_1,\ldots,\lambda_{n-1}$ are all equal, and that it
> is symmetric about $0$ ([Ib16, Section 3.7], [RaVa15, Proposition 2.8]). A canonical minimiser
> exists ([RaVa15, Section 2]) and must equioscillate ([Ki77], [Ib16, Section 3.7]), so there is
> exactly one such node set, and hence a unique canonical minimiser of $\Lambda$.

```lean
theorem erdos_1129.variants.unique (n : ℕ) (hn : 2 ≤ n) :
    ∃! x : Fin n → ℝ, IsCanonical x ∧ Equioscillates x
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L180).

## `Erdos1129.erdos_1129.variants.free_nodes_not_unique`

Solved: stated here without proof.

> Without the canonical hypothesis the minimiser of $\Lambda$ is not unique. For every $n\ge 3$
> there are uncountably many node sets $x_1\lt \dots\lt x_n$ in $[-1,1]$ with the minimal Lebesgue
> constant [RaVa15, Theorem 2.5]. The reason is affine invariance. Rescaling a node set to a
> canonical one keeps its local maxima between consecutive nodes and does not increase $\Lambda$
> ([Ib16, Section 2.1 (e)]), so the minimal Lebesgue constant $\Lambda^*$ is attained by the
> canonical minimiser $x^*$. The shrunk node set $x^*/\tau$ with $\tau\ge 1$ has
> $\Lambda(x^*/\tau)=\max_{\lvert u\rvert\le\tau}L_{x^*}(u)$. Since $L_{x^*}(\pm 1)=1\lt \Lambda^*$ for
> $n\ge 3$, this is still $\Lambda^*$ for all $\tau\ge 1$ close to $1$ (see the proof of
> [RaVa15, Theorem 2.5]). For $n=4$ the node sets
> $\pm 1/\tau,\pm t/\tau$ with $1\le\tau\le b$ for a constant $b\approx 1.0433$, where $t$ is as
> in `erdos_1129.variants.four_nodes`, are all optimal [RaVa15, Theorem 4.2].

```lean
theorem erdos_1129.variants.free_nodes_not_unique (n : ℕ) (hn : 3 ≤ n) :
    ¬ {x : Fin n → ℝ | IsMinimiser x}.Countable
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L198).

## `Erdos1129.erdos_1129.variants.three_nodes`

Solved: stated here without proof.

> For $n=3$ the canonical minimiser is $-1,0,1$, with $\Lambda=\frac54$ (Bernstein [Be31], see
> [RaVa15, Section 2]).

```lean
theorem erdos_1129.variants.three_nodes :
    {x : Fin 3 → ℝ | IsCanonical x ∧ IsMinimiser x} = ({![(-1 : ℝ), 0, 1]} : Set (Fin 3 → ℝ)) ∧
      lebesgueConstant (![(-1 : ℝ), 0, 1] : Fin 3 → ℝ) = 5 / 4
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L207).

## `Erdos1129.erdos_1129.variants.four_nodes`

Solved: stated here without proof.

> For $n=4$ the canonical minimiser is $-1,-t,t,1$, where $t>0$ is the (unique positive) root of
> $25t^6+17t^4+2t^2-1$, so $t\approx 0.4178$, and
> $\Lambda=\frac{1+t^2}{1-t^2}\approx 1.4229$ [RaVa15, Section 3, (3.4)-(3.9)].

```lean
theorem erdos_1129.variants.four_nodes (t : ℝ) (ht : 0 < t)
    (hroot : 25 * t ^ 6 + 17 * t ^ 4 + 2 * t ^ 2 - 1 = 0) :
    {x : Fin 4 → ℝ | IsCanonical x ∧ IsMinimiser x} =
        ({![(-1 : ℝ), -t, t, 1]} : Set (Fin 4 → ℝ)) ∧
      lebesgueConstant (![(-1 : ℝ), -t, t, 1] : Fin 4 → ℝ) = (1 + t ^ 2) / (1 - t ^ 2)
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L218).

## `Erdos1129.erdos_1129.variants.erdos_lower_bound`

Solved: stated here without proof.

> Faber [Fa14] proved $\Lambda(x_1,\ldots,x_n)\gg \log n$ for all choices of $x_i$, and Bernstein
> [Be31] announced $\Lambda>(\frac{2}{\pi}-o(1))\log n$ (see [Er61c, p. 235]). Erdős [Er61c,
> Theorem 1] improved this: there is an absolute constant $c_1$ such that for all
> $-1\le x_1\lt \cdots\lt x_n\le 1$
>
> $$\max_{x\in[-1,1]}\sum_k\lvert l_k(x)\rvert>\frac{2}{\pi}\log n-c_1.$$

```lean
theorem erdos_1129.variants.erdos_lower_bound :
    ∃ C : ℝ, ∀ (n : ℕ) (x : Fin n → ℝ), 1 ≤ n → IsNodeSet x →
      2 / Real.pi * Real.log n - C < lebesgueConstant x
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 233](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L233).

## `Erdos1129.erdos_1129.variants.chebyshev_upper_bound`

Solved: stated here without proof.

> This is best possible: for the zeros of the Chebyshev polynomial $T_n$ there is an absolute
> constant $c_2$ with $\max_{x\in[-1,1]}\sum_k\lvert l_k(x)\rvert\lt \frac{2}{\pi}\log n+c_2$
> ([Er61c, p. 236], [Er67, p. 66]). [Ib16, Section 3.2] gives the precise asymptotics.

```lean
theorem erdos_1129.variants.chebyshev_upper_bound :
    ∃ C : ℝ, ∀ (n : ℕ) (x : Fin n → ℝ), 1 ≤ n → IsChebyshevNodes x →
      lebesgueConstant x < 2 / Real.pi * Real.log n + C
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1129.lean, line 244](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean#L244).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1129.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1129.lean)
- [erdosproblems.com/1129](https://www.erdosproblems.com/1129)
