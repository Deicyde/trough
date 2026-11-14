---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.triangle_complete, MIPRE.Tailored.AnsRed.triangle_sound, MIPRE.Tailored.AnsRed.decSat_iff
statement: formalized
proof: formalized
---

# Triangulation and decoupling; rem:prop_triangulated_system

If the equations have at most $N$ variables, all below $N$, the extension of a solution solves the triangulated system; a solution of the triangulated system solves the equations. Five assignments solve the decoupled system exactly when the first two agree with the first copy, the three copies agree on $[\ell]$, and the triangulated equations hold on the three copies.

## Depends on

- [Purified, triangulated and decoupled systems](def-ar-linear.md)

## Proof

The step equations of a row force the partial sums, by induction along the row, and the last one is the row. For the decoupled system, each kind of equation is one instance of the indicator, and conversely every instance is one of the kinds.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.triangle_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.triangle_complete), [`MIPRE.Tailored.AnsRed.triangle_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.triangle_sound), [`MIPRE.Tailored.AnsRed.decSat_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.decSat_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2372](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2372)
