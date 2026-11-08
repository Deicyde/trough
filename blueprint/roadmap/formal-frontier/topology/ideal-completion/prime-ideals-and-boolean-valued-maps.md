---
declaration: def
origin: cited
lean: Order.Ideal.primeEquivBoolHom
statement: formalized
---

# Prime ideals and Boolean-valued maps

For `[Lattice A]` and
`[BoundedOrder A]`,
[`Order.Ideal.primeEquivBoolHom`](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/PrimeIdeal.lean)
identifies prime order ideals with bounded lattice homomorphisms `A → Bool`.
The characteristic map sends precisely the ideal to `false`; conversely
[`BoundedLatticeHom.falseIdeal`](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/PrimeIdeal.lean)
is its prime false fiber. Every such map is surjective. This includes the
one-element lattice, for which both sides of the equivalence are empty.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/README.md#headline-results) of [FormalFrontier/ideal-completion](https://github.com/FormalFrontier/ideal-completion) at commit [e316d02a](https://github.com/FormalFrontier/ideal-completion/tree/e316d02a1c0814b130a7085a112c142542b7019d), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.Ideal.primeEquivBoolHom` (def), declared in [IdealCompletion/PrimeIdeal.lean, line 131](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/PrimeIdeal.lean#L131).

Read from the source at commit [e316d02a](https://github.com/FormalFrontier/ideal-completion/tree/e316d02a1c0814b130a7085a112c142542b7019d), without running Lean.

## Sources

- [ideal-completion at e316d02a: README, headline results](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/README.md#headline-results)
- [Source of `Order.Ideal.primeEquivBoolHom` in IdealCompletion/PrimeIdeal.lean](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/PrimeIdeal.lean#L131)
