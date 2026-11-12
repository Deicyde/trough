---
declaration: section
origin: cited
lean: OAI.Lech.dutta_domain
statement: formalized
proof: formalized
---

# 194. Lech’s multiplicity conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves $e(R)\le e(S)$ for every flat local homomorphism of nonzero Noetherian local rings, where *e* is Hilbert–Samuel multiplicity. This resolves Lech's conjecture in every dimension and characteristic.

## Lech's multiplicity conjecture

We prove Lech's multiplicity conjecture: Hilbert–Samuel multiplicity cannot decrease under a flat local homomorphism of nonzero Noetherian local rings. The result holds in arbitrary dimension, with no restrictions on the residue fields or characteristics.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Lechs-multiplicity-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Lech's multiplicity conjecture compares Hilbert–Samuel multiplicities across flat local maps. The linked formalization covers a supporting characteristic-$p$ comparison over a complete Noetherian local domain $D$: for a complex satisfying the stated short-complex and finite-length homology conditions, its Frobenius multiplicity sequence converges to its Dutta multiplicity, and the Hilbert–Samuel multiplicity of $D$ is at most that Dutta multiplicity.

This selected statement is the complete-domain Dutta comparison. The paper's full flat-local result in arbitrary characteristic is outside it.

## Lean: Complete-domain Dutta multiplicity comparison

Stated in [DuttaDomain.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DuttaDomain.lean).

```lean
theorem dutta_domain : DuttaDomainClaim.{u}
```

Proved in [lean/OAI/RingTheory/Multiplicity/DuttaDomain.lean, line 46](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/Multiplicity/DuttaDomain.lean#L46).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/194.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/194.md)
