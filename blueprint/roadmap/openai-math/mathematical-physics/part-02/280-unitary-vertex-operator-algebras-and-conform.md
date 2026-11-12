---
declaration: section
origin: cited
lean: OAI.MinimalVertex.main
statement: formalized
proof: formalized
---

# 280. Unitary vertex operator algebras and conformal nets

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the strongly rational case of the strong-locality conjecture: every simple unitary strongly rational complex vertex operator algebra generates a completely rational conformal net. Its simple modules are unitarizable, and its representation category agrees with the net’s finite-index sectors as a braided unitary tensor category.

## Strongly rational unitary vertex operator algebras and conformal nets

Every simple unitary strongly rational vertex operator algebra generates a completely rational conformal net. All its simple grading-restricted modules are unitarizable, its canonical fusion forms are positive, and the Carpi–Weiner–Xu functor gives a braided unitary tensor equivalence from its grading-restricted finite-length module category onto the finite-index sectors of the net. Gui's extension theorems then identify normalized irreducible finite-index local extensions of these nets with simple CFT-type conformal extensions of the vertex operator algebras.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The linked formalization proves the first construction step relating strongly rational unitary vertex operator algebras to conformal nets. For a simple unitary strongly rational vertex operator algebra, it establishes polynomial energy bounds and strong locality and constructs an irreducible conformal net with the stated covariance, vacuum, and positive-energy properties.

The selected statement does not include complete rationality of the net, unitarizability of all simple modules, the braided tensor equivalence, or the classification of local extensions described in the paper.

## Lean: Energy bounds, strong locality, and an irreducible conformal net

Stated in [VertexAlgebraNet.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VertexAlgebraNet.lean).

```lean
theorem main (_hSimple : A.toVertexAlgebra.IsSimple)
    (hSR : A.IsStronglyRational.{u,v}) :
    A.PolynomialEnergyBounds ∧ OAI.MinimalVertex.CKLWStrongLocal U hSR.2.2 ∧
      Nonempty (OAI.MinimalVertex.IrreducibleConformalNetStructure (OAI.MinimalVertex.intervalAlgebra U hSR.2.2))
```

Proved in [lean/OAI/RepresentationTheory/VertexAlgebra/MinimalComparator.lean, line 676](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/VertexAlgebra/MinimalComparator.lean#L676).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/280.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/280.md)
