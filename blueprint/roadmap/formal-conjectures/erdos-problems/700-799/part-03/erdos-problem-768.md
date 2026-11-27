---
declaration: theorem
origin: cited
lean: Erdos768.erdos_768
statement: formalized
---

# Erdős Problem 768

> *References:*
> - [erdosproblems.com/768](https://www.erdosproblems.com/768)
> - [Er74b] Erdős, P., *Remarks on some problems in number theory*.
>   Math. Balkanica (1974), 197–202.

*Quoted from [FormalConjectures/ErdosProblems/768.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/768.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/768](https://www.erdosproblems.com/768).

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `Erdos768.erdos_768`

Open: stated without proof.

> Let $A \subset \mathbb{N}$ be the set of $n$ such that for every prime $p \mid n$ there is
> some $d \mid n$ with $d>1$ and $d \equiv 1 \pmod p$. Is there a constant $c>0$ such that,
> for all large $N$,
>
> $$\frac{\lvert A\cap[1,N]\rvert}{N}=
> \exp\big(-(c+o(1))\sqrt{\log N}\log\log N\big)?$$

```lean
theorem erdos_768 : ∃ c > 0, ∃ error : ℕ → ℝ,
    error =o[atTop] (fun _ ↦ (1 : ℝ)) ∧ ∀ᶠ N in atTop,
      erdos768Density N = Real.exp (-(c + error N) * erdos768Scale N)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/768.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/768.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/768.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/768.lean)
- [erdosproblems.com/768](https://www.erdosproblems.com/768)
