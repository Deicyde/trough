---
declaration: theorem
origin: cited
lean: Erdos969.erdos_969, Erdos969.erdos_969.variants.prime_number_theorem, Erdos969.erdos_969.variants.evelyn_linfoot
statement: formalized
---

# Erdős Problem 969

> *References:*
> - [Erdős Problem 969](https://www.erdosproblems.com/969)
> - Moser, L. and MacLeod, R. A., *The error term for the squarefree integers*.
>   Canadian Mathematical Bulletin **9** (1966), 303–306.
>   https://doi.org/10.4153/CMB-1966-039-4

*Quoted from [FormalConjectures/ErdosProblems/969.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/969.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/969](https://www.erdosproblems.com/969).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos969.erdos_969`

Open: stated without proof.

> Let $Q(x)$ count the squarefree integers in $[1,x]$, and define $E(x)$ by
>
> $$Q(x)=\frac{6}{\pi^2}x+E(x).$$
>
> Determine the order of magnitude of $E(x)$: an upper bound $E(x)=O(g(x))$ with a matching
> oscillation bound $E(x)\ne o(g(x))$.

```lean
theorem erdos_969 :
    let g := erdos_969.answer
    (fun x => |squarefreeCountingError x|) =O[atTop] g ∧
      ¬(fun x => |squarefreeCountingError x|) =o[atTop] g
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/969.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/969.lean#L57).

## `Erdos969.erdos_969.variants.prime_number_theorem`

Solved: stated here without proof.

> The prime number theorem implies $E(x)=o(\sqrt{x})$.

```lean
theorem erdos_969.variants.prime_number_theorem :
    (fun x => |squarefreeCountingError x|) =o[atTop] (fun x : ℕ => (x : ℝ).sqrt)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/969.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/969.lean#L65).

## `Erdos969.erdos_969.variants.evelyn_linfoot`

Solved: stated here without proof.

> Evelyn and Linfoot proved $E(x)=\Omega(x^{1/4})$.

```lean
theorem erdos_969.variants.evelyn_linfoot :
    ¬(fun x => |squarefreeCountingError x|) =o[atTop]
      (fun x : ℕ => (x : ℝ) ^ (1 / 4 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/969.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/969.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/969.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/969.lean)
- [erdosproblems.com/969](https://www.erdosproblems.com/969)
