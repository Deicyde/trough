---
declaration: section
origin: cited
lean: OAI.ThreeTorus.simple_lebesgue_spectrum
statement: formalized
proof: formalized
---

# 144. Banach’s simple Lebesgue-spectrum problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the probability-preserving form of Banach's simple Lebesgue-spectrum problem within smooth dynamics. A smooth volume-preserving diffeomorphism of the standard-volume three-torus has simple Lebesgue spectrum on its entire complex mean-zero $L^{2}$ space: the bilateral iterates of one real observable form an orthonormal basis of that space.

## A smooth three-torus diffeomorphism with simple Lebesgue spectrum

We solve the probability-preserving form of Banach's simple Lebesgue-spectrum problem in smooth dynamics. We construct a $C^{∞}$ diffeomorphism of the three-torus that preserves standard volume and whose Koopman operator has simple Lebesgue spectrum on the entire mean-zero $L^{2}$ space.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Banach's simple Lebesgue-spectrum problem asks for a probability-preserving transformation with simple Lebesgue spectrum on its mean-zero $L^2$ space. The formalization constructs a smooth volume-preserving diffeomorphism of the three-torus with this property. It gives a real-valued cyclic vector whose integer iterates form an orthonormal basis of the entire mean-zero space, and an isometric identification under which the Koopman operator becomes multiplication by the coordinate function on the circle. The transformation is also ergodic.

## Lean: Smooth simple Lebesgue spectrum on the three-torus

Stated in [ThreeTorus.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThreeTorus.lean).

```lean
theorem simple_lebesgue_spectrum : MainConclusion
```

Proved in [lean/OAI/Dynamics/ThreeTorus/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/ThreeTorus/Main.lean#L17).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/144.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/144.md)
