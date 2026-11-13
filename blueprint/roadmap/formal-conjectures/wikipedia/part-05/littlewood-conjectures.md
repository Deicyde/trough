---
declaration: theorem
origin: cited
lean: LittlewoodConjecture.littlewood_conjecture, LittlewoodConjecture.padic_littlewood_conjecture
statement: formalized
---

# Littlewood conjectures

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Littlewood_conjecture)
> - [Bernard de Mathan and Olivier Teulié, *Problèmes diophantiens simultanés*](https://doi.org/10.1007/s00605-003-0199-y)

*Quoted from [FormalConjectures/Wikipedia/LittlewoodConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LittlewoodConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `LittlewoodConjecture.littlewood_conjecture`

Open: stated without proof.

> For any two real numbers $\alpha$ and $\beta$,
>
> $$
>   \liminf_{n\to\infty} n\||n\alpha\||\||n\beta\|| = 0
> $$
>
> where $\||x\|| := \min(|x - \lfloor x \rfloor|, |x - \lceil x \rceil|)$ is the distance
> to the nearest integer.

```lean
theorem littlewood_conjecture (α β : ℝ) :
    atTop.liminf (fun (n : ℕ) ↦ n * distToNearestInt (n * α) * distToNearestInt (n * β)) = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LittlewoodConjecture.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LittlewoodConjecture.lean#L46).

## `LittlewoodConjecture.padic_littlewood_conjecture`

Open: stated without proof.

> For real number $\alpha$ and prime $p$,
>
> $$
>   \liminf\_{n \to\infty} n |n|\_{p}\||n\alpha\|| = 0
> $$
>
> where $\||x\|| := \min(|x - \lfloor x \rfloor|, |x - \lceil x \rceil|)$ is the distance
> to the nearest integer, and $|x|\_{p}$ is the $p$-adic norm.

```lean
theorem padic_littlewood_conjecture (α : ℝ) (p : ℕ) (hp : p.Prime) :
    atTop.liminf (fun (n : ℕ) ↦ n * padicNorm p n * distToNearestInt (n * α)) = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LittlewoodConjecture.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LittlewoodConjecture.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LittlewoodConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LittlewoodConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Littlewood_conjecture)
