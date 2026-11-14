---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.extend_complete, MIPRE.Tailored.AnsRed.decSat_sound, MIPRE.Tailored.AnsRed.decSat_of_accepts, MIPRE.Tailored.AnsRed.accepts_of_decSat
statement: formalized
proof: formalized
---

# The extension; cor:triang_and_decoupling_extend

Let $\Delta$ be at least the number of equations times $N = \ell_A + \ell_B$. A solution $f$ gives the solution $(f, f(\ell_A + \cdot), \mathrm{ext}\, f, \mathrm{ext}\, f, \mathrm{ext}\, f)$ of the decoupled triangulated system on $\ell = N + \Delta$, and the first two blocks of any solution, glued, solve the equations. For the canonical decider (claim:properties\_of\_L\*, item 2): if the game accepts answers of the right lengths, the extension of the table of their linear parts solves the decoupled triangulated purified system, the last three blocks linear in the linear answers with coefficients depending only on the readable ones; and if five assignments solve that system, the game accepts the readable answers completed by the first two blocks, read at the linear lengths.

## Depends on

- [Purification; fact:completeness_and_soundness_purification](lem-ar-purification.md)
- [Triangulation and decoupling; rem:prop_triangulated_system](lem-ar-triangle-decouple.md)

## Proof

Lemma [Triangulation and decoupling; rem:prop_triangulated_system](lem-ar-triangle-decouple.md): the extension agrees with $f$ below $N$, and every triangulated equation is below $N + \Delta$, so the three copies of a solution solve the triangulated system and hence the equations. Lemma [Purification; fact:completeness_and_soundness_purification](lem-ar-purification.md) translates between the equations and the decider.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.extend_complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.extend_complete), [`MIPRE.Tailored.AnsRed.decSat_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.decSat_sound), [`MIPRE.Tailored.AnsRed.decSat_of_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.decSat_of_accepts), [`MIPRE.Tailored.AnsRed.accepts_of_decSat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_of_decSat).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2391](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2391)
