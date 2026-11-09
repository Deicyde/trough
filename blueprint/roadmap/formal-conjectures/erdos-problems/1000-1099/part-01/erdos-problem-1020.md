---
declaration: theorem
origin: cited
lean: Erdos1020.erdos_1020
statement: formalized
---

# Erdős Problem 1020

> *References:*
> - [erdosproblems.com/1020](https://www.erdosproblems.com/1020)
> - [BDE76] Bollobás, B. and Daykin, D. E. and Erdős, P., *Sets of independent edges of a hypergraph*.
>   Quart. J. Math. Oxford Ser. (2) (1976), 25--32.
> - [Er65d] Erdős, P., *A problem on independent {$r$}-tuples*. Ann. Univ. Sci. Budapest. Eötvös Sect.
>   Math. (1965), 93--95.
> - [ErGa59] Erdős, P. and Gallai, T., *On maximal paths and circuits of graphs*. Acta Math. Acad.
>   Sci. Hungar. (1959), 337-356 (unbound insert).
> - [FLM12] Frankl, Peter and Łuczak, Tomasz and Mieczkowska, Katarzyna, *On matchings in
>   hypergraphs*. Electron. J. Combin. (2012), Paper 42, 5.
> - [FRR12] Frankl, Peter and Rödl, Vojtech and Ruciński, Andrzej, *On the maximum number of edges in
>   a triple system not containing a disjoint family of a given size*. Combin. Probab. Comput. (2012),
>   141--148.
> - [Fr17] Frankl, Peter, *Proof of the {E}rdős matching conjecture in a new range*. Israel J. Math.
>   (2017), 421--430.
> - [Fr87] Frankl, Peter, *The shifting technique in extremal set theory*. (1987), 81--110.
> - [HLS12] Huang, Hao and Loh, Po-Shen and Sudakov, Benny, *The size of a hypergraph and its matching
>   number*. Combin. Probab. Comput. (2012), 442--450.
> - [Kl68] Kleitman, Daniel J., *Maximal number of subsets of a finite set no {$k$} of which are
>   pairwise disjoint*. J. Combinatorial Theory (1968), 157--163.
> - [KoKu23] Kolupaev, Dmitriy and Kupavskii, Andrey, *Erdős matching conjecture for almost perfect
>   matchings*. Discrete Math. (2023), Paper No. 113304, 9.
> - [LuMi14] Łuczak, Tomasz and Mieczkowska, Katarzyna, *On {E}rdős' extremal problem on matchings in
>   hypergraphs*. J. Combin. Theory Ser. A (2014), 178--194.

*Quoted from [FormalConjectures/ErdosProblems/1020.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1020.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1020](https://www.erdosproblems.com/1020).

The file states 1 research or textbook statement: 1 open.

## `Erdos1020.erdos_1020`

Open: stated without proof.

> Let $f(n;r,k)$ be the maximal number of edges in an $r$-uniform hypergraph which contains no set of $k$ many independent edges.
>
> For all $r\geq 3$, $$f(n;r,k)=\max\left(\binom{rk-1}{r}, \binom{n}{r}-\binom{n-k+1}{r}\right).$$
>
> Note: the source states the formula with no range on `n` or `k`, but some restriction
> is needed: e.g. for `r = 3`, `k = 2`, `n = 4` no two disjoint triples fit in `4`
> vertices, so the left-hand side is `4.choose 3 = 4` while the right-hand side is
> `5.choose 3 = 10`. We require `k ≥ 1` and `n ≥ r*k - 1`: this is the smallest `n`
> accommodating the construction counted by the first term (all `r`-subsets of a fixed
> `(r*k - 1)`-set), and at `n = r*k - 1` the equality holds trivially, since the complete
> `r`-uniform hypergraph has no `k`-matching. The source's commentary likewise calls the
> case `n < k*r` trivial.

```lean
theorem erdos_1020 (r : ℕ) (hr : 3 ≤ r) (n k : ℕ) (hk : 0 < k)
    (hrk : r * k - 1 ≤ n) :
    f n r k = max ((r * k - 1).choose r)
      (n.choose r - (n - k + 1).choose r)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1020.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1020.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1020.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1020.lean)
- [erdosproblems.com/1020](https://www.erdosproblems.com/1020)
