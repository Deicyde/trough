---
declaration: section
origin: cited
lean: IsIntegrallyClosed.isDomain_and_isIntegrallyClosed_of_flat_of_isLocalHom, Module.length_quotient_le_of_ker_le
statement: formalized
proof: formalized
---

# Local rings, dimension and completion: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/index.html).

Local rings and their residue fields, Krull dimension, adic completion, regular local rings and length of modules.

## Flat local maps reflect integrally closed domains

A flat local homomorphism from a local ring to a domain and integrally
closed local ring forces the source to be a domain and integrally closed.
The flatness is stated with the `Flat` class of Mathlib 4.35, where the
FLT source used the older `RingHom.Flat` spelling.

Formalized by `IsIntegrallyClosed.isDomain_and_isIntegrallyClosed_of_flat_of_isLocalHom`, a theorem declared in [MathlibExt/RingTheory/IntegrallyClosed/FlatLocalHom.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/IntegrallyClosed/FlatLocalHom.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/index.html#is-domain-and-is-integrally-closed-of-fl).

## Length bound for a quotient containing a kernel

If `ker f ≤ K`, the length of `M ⧸ K` is at most the length of `N`.

Formalized by `Module.length_quotient_le_of_ker_le`, a theorem declared in [MathlibExt/RingTheory/Length.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Length.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/index.html#length-quotient-le-of-ker-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local rings, dimension and completion](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/local-rings)
