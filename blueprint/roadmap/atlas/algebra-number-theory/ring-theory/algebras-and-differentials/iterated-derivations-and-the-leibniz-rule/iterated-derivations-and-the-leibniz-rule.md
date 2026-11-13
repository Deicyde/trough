---
declaration: section
origin: cited
lean: Derivation.iterate_pow_of_apply_eq_smul_sq
statement: formalized
proof: formalized
---

# Iterated derivations and the Leibniz rule: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/iterated-derivations-and-the-leibniz-rule/index.html).

## Iterated derivation of a power when $D\varepsilon = r\varepsilon^2$

If `D epsilon = r • epsilon²`, then the `n`th iterate of `D` on `epsilon^m` has
coefficient `r^n` times the ascending factorial of `m`. The coefficient is not cancelled,
so the formula remains valid in positive characteristic.

Formalized by `Derivation.iterate_pow_of_apply_eq_smul_sq`, a theorem declared in [MathlibExt/RingTheory/Derivation/IteratePower.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Derivation/IteratePower.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/iterated-derivations-and-the-leibniz-rule/index.html#iterate-pow-of-apply-eq-smul-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Iterated derivations and the Leibniz rule](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/iterated-derivations-and-the-leibniz-rule/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/algebras-and-differentials/iterated-derivations-and-the-leibniz-rule)
