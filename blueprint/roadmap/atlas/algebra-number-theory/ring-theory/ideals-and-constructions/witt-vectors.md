---
declaration: section
origin: cited
lean: WittVector.coeff_eq_coeff_of_forall_ghostComponent_eq, WittVector.exists_forall_ghostComponent_eq_of_sub_frobeniusLift_mem, WittVector.ringHom_map_frobenius_of_finite, WittVector.coeff_mem_span_of_ghostComponent_mem_span_pow_of_isReduced
statement: formalized
proof: formalized
---

# Witt vectors

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html).

## Ghost components determine Witt vector coefficients

Ghost components determine Witt vector coefficients when `p` is a
non-zero-divisor.

Formalized by `WittVector.coeff_eq_coeff_of_forall_ghostComponent_eq`, a theorem declared in [MathlibExt/RingTheory/WittVector/Basic.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/WittVector/Basic.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html#coeff-eq-coeff-of-forall-ghost-component).

## Ghost data compatible with a Frobenius lift come from a Witt vector

Compatible ghost data with a Frobenius lift is realized by a Witt
vector.

Formalized by `WittVector.exists_forall_ghostComponent_eq_of_sub_frobeniusLift_mem`, a theorem declared in [MathlibExt/RingTheory/WittVector/Basic.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/WittVector/Basic.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html#exists-forall-ghost-component-eq-of-sub).

## Homomorphisms from Witt vectors over finite fields commute with Frobenius

Ring homomorphisms out of Witt vectors over a finite field commute with
Frobenius.

Formalized by `WittVector.ringHom_map_frobenius_of_finite`, a theorem declared in [MathlibExt/RingTheory/WittVector/Basic.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/WittVector/Basic.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html#ring-hom-map-frobenius-of-finite).

## Divisibility of Witt coefficients from divisible ghost components

If a ghost component of a Witt vector is highly `p`-divisible and the
reduction mod `p` is reduced, all lower coefficients lie in `(p)`.

Formalized by `WittVector.coeff_mem_span_of_ghostComponent_mem_span_pow_of_isReduced`, a theorem declared in [MathlibExt/RingTheory/WittVector/Basic.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/WittVector/Basic.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html#coeff-mem-span-of-ghost-component-mem-sp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Witt vectors](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/witt-vectors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ideals-and-constructions/witt-vectors)
