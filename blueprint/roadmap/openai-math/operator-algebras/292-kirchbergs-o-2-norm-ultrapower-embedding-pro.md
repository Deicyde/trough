---
declaration: section
origin: cited
lean: OAI.NuclearUltrapower.main_no_embedding
statement: formalized
proof: formalized
---

# 292. Kirchberg's $\mathcal O_2$ norm-ultrapower embedding problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs an explicit separable unital full group $C^{∗}$-algebra that cannot embed unitally into the norm ultrapower of any fixed nonzero unital nuclear $C^{∗}$-algebra, for any free ultrafilter on the natural numbers. Taking the target to be $\mathcal O_2$ answers Kirchberg's norm-ultrapower embedding problem negatively.

## An explicit obstruction to nuclear norm-ultrapower embeddings

We give a negative answer to Kirchberg's norm-ultrapower embedding problem. We construct an explicit separable unital full group $C^{∗}$-algebra that admits no unital embedding into $B^{ω}$, for any nonzero unital nuclear $C^{∗}$-algebra *B* and any free ultrafilter *ω* on ℕ. In particular, it does not embed unitally into $\mathcal O_2^\omega$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kirchberg's norm-ultrapower embedding problem asks whether separable $C^*$-algebras embed into norm ultrapowers of nuclear algebras. The formalization constructs an explicit separable unital full group $C^*$-algebra that has no unital embedding into $B^\omega$ for any nonzero unital nuclear $C^*$-algebra $B$ and any free ultrafilter $\omega$ on $\mathbb N$. In particular, it does not embed unitally into an ultrapower of the Cuntz algebra $\mathcal O_2$.

## Lean: Obstruction to nuclear norm-ultrapower embeddings

```lean
theorem main_no_embedding : MainStatementWithCuntzCorollary.{0}
```

Stated in [NuclearUltrapower.lean, line 208](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/NuclearUltrapower.lean#L208). Proved in [lean/OAI/Analysis/NuclearUltrapower/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/NuclearUltrapower/Main.lean#L14).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/292.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/292.md)
