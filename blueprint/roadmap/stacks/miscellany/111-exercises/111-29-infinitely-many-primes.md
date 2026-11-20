---
declaration: section
origin: cited
lean: Polynomial.monic_aeval_isFiniteLocallyFreeOfRank_int, Polynomial.monic_aeval_isFiniteLocallyFreeOfRank_zmod
statement: formalized
proof: formalized
---

# 111.29 Infinitely many primes

Section 111.29 of the Stacks Project, [Tag 0286](https://stacks.math.columbia.edu/tag/0286). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 02ER, a remark

[Tag 02ER](https://stacks.math.columbia.edu/tag/02ER) in the Stacks Project.

**`Polynomial.monic_aeval_isFiniteLocallyFreeOfRank_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/PolynomialSubstitution.lean, line 142](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Exercises/PolynomialSubstitution.lean#L142). The attribute's comment: “part (1)”.

> Substitution by a monic integral polynomial of positive degree is finite locally free
> of rank equal to its degree.

```lean
theorem monic_aeval_isFiniteLocallyFreeOfRank_int (h : Polynomial ℤ)
    (hh : h.Monic) (hd : 0 < h.natDegree) :
    letI : Algebra (Polynomial ℤ) (Polynomial ℤ) := (Polynomial.aeval h).toRingHom.toAlgebra
    letI : Module (Polynomial ℤ) (Polynomial ℤ) := Algebra.toModule
    Module.IsFiniteLocallyFreeOfRank (Polynomial ℤ) (Polynomial ℤ) h.natDegree
```

**`Polynomial.monic_aeval_isFiniteLocallyFreeOfRank_zmod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/PolynomialSubstitution.lean, line 152](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Exercises/PolynomialSubstitution.lean#L152). The attribute's comment: “part (2)”.

> After reduction modulo a prime, substitution by the reduced monic polynomial is
> finite locally free of the original degree.

```lean
theorem monic_aeval_isFiniteLocallyFreeOfRank_zmod (h : Polynomial ℤ)
    (hh : h.Monic) (hd : 0 < h.natDegree) (p : ℕ) (hp : p.Prime) :
    let g : Polynomial (ZMod p) := h.map (Int.castRingHom (ZMod p))
    letI : Algebra (Polynomial (ZMod p)) (Polynomial (ZMod p)) :=
      (Polynomial.aeval g).toRingHom.toAlgebra
    letI : Module (Polynomial (ZMod p)) (Polynomial (ZMod p)) := Algebra.toModule
    Module.IsFiniteLocallyFreeOfRank (Polynomial (ZMod p))
      (Polynomial (ZMod p)) h.natDegree
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.29, Tag 0286](https://stacks.math.columbia.edu/tag/0286)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
