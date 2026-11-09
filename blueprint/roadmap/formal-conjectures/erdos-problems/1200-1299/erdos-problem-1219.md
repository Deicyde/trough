---
declaration: theorem
origin: cited
lean: Erdos1219.erdos_1219
statement: formalized
---

# Erdős Problem 1219

> *References:*
> - [erdosproblems.com/1219](https://www.erdosproblems.com/1219)
> - [ErHa71] Erdős, Paul and Hajnal, András, Unsolved problems in set theory. Axiomatic Set
>   Theory, Proc. Sympos. Pure Math. XIII Part I (1971), 17-48.
> - [Ko25b] Komjáth, Péter, The Erdős–Hajnal problem list. Bull. Symb. Log. (2025), 418-461.
> - [Sh75] Shelah, Saharon, Notes on partition calculus. Infinite and finite sets (Colloq.,
>   Keszthely, 1973), Colloq. Math. Soc. János Bolyai 10, North-Holland (1975), 1257-1276.

*Quoted from [FormalConjectures/ErdosProblems/1219.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1219.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1219](https://www.erdosproblems.com/1219).

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1219.erdos_1219`

Solved: stated here; a Lean proof is at [https://github.com/jbaelaw/erdos1219-lean/blob/00e696a9cd2bbd8cad33d2cdc90ad385058c1466/Solution.lean#L22](https://github.com/jbaelaw/erdos1219-lean/blob/00e696a9cd2bbd8cad33d2cdc90ad385058c1466/Solution.lean#L22).

> Let $(n_k)$ be an increasing sequence of integers such that $2^{\aleph_{n_k}}$ is strictly
> increasing, and $2^{\aleph_{n_0}} > \aleph_\omega$. Is it true that
> $$\sum_k 2^{\aleph_{n_k}} \to (\aleph_\omega)^2?$$
>
> Here $\sum_k 2^{\aleph_{n_k}}$ is the cardinal sum, and the partition relation is the classical
> one with two colours: every $2$-colouring of the pairs of a set of that cardinality has a
> monochromatic set of cardinality $\aleph_\omega$.
>
> A problem of Erdős, Hajnal, and Rado [ErHa71], proved by Shelah [Sh75].

```lean
theorem erdos_1219 :
    ∀ n : ℕ → ℕ, StrictMono n →
      StrictMono (fun k => (2 : Cardinal.{u}) ^ ℵ_ (n k)) →
      ℵ_ ω < (2 : Cardinal.{u}) ^ ℵ_ (n 0) →
      cardinalPartitionRel (sum fun k => (2 : Cardinal.{u}) ^ ℵ_ (n k)) 2 2 (fun _ => ℵ_ ω)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1219.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1219.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1219.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1219.lean)
- [erdosproblems.com/1219](https://www.erdosproblems.com/1219)
