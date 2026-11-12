---
declaration: section
origin: cited
lean: OAI.QuinticLienard.main
statement: formalized
proof: formalized
---

# 143. Hilbert's sixteenth problem: uniform bounds for limit cycles

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the uniform boundedness assertion in Hilbert's sixteenth problem: the number of isolated periodic orbits of a real planar polynomial vector field is bounded by a finite constant depending only on its degree. For classical quintic Liénard systems, the exact maximum is two limit cycles.

## Uniform bounds for planar polynomial limit cycles

For every degree, we prove that the number of isolated periodic orbits of a real planar polynomial vector field is bounded by a finite constant depending only on that degree. This establishes the uniform boundedness assertion in the second part of Hilbert's sixteenth problem. The proof uses separation of asymptotic expansions on nested complex domains and a finite-dimensional counting argument.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf).

## Two limit cycles for quintic Liénard systems

Every classical Liénard system $\dot x=y-F(x)$, $\dot y=-x$, with *F* an arbitrary real polynomial of degree at most five, has at most two geometrically distinct isolated periodic orbits, and the bound is attained. This proves the degree-five case of the Lins Neto–de Melo–Pugh conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

For the quintic Liénard system $x'=y-F(x)$, $y'=-x$, the formalized result proves that every real polynomial $F$ of degree at most five yields at most two limit cycles, and that some such $F$ yields exactly two. Limit cycles are isolated images of nonconstant periodic solutions. No sign, parity, hyperbolicity, or amplitude restriction is imposed.

## Lean: Exact two-cycle bound for quintic Liénard systems

Stated in [QuinticLienard.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QuinticLienard.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    (∀ F : Polynomial ℝ, F.degree ≤ 5 → {C : Set Plane | IsLimitCycle F C}.encard ≤ 2) ∧
    (∃ F : Polynomial ℝ, F.degree ≤ 5 ∧ {C : Set Plane | IsLimitCycle F C}.encard = 2)
```

Proved in [lean/OAI/Analysis/LienardCycles/Main.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LienardCycles/Main.lean#L20).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/143.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/143.md)
