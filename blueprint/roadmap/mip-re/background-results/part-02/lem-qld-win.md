---
declaration: lemma
origin: cited
lean: MIPRE.QLD.subtest_le, MIPRE.QLD.agree_subtest_le, MIPRE.QLD.item_consistency, MIPRE.QLD.item_lowDeg_aline, MIPRE.QLD.item_lowDeg_dline, MIPRE.QLD.item_pauli_consistency, MIPRE.QLD.item_commutation, MIPRE.QLD.item_commutation_consistency, MIPRE.QLD.item_ms_consistency_X, MIPRE.QLD.item_ms_consistency_Z, MIPRE.QLD.msPOVM, MIPRE.QLD.msEps, MIPRE.QLD.condFail_ms_le, MIPRE.QLD.one_sub_povmValue_ms_le, MIPRE.QLD.sum_msEps_le, MIPRE.QLD.item_magicSquare, MIPRE.QLD.isPVMIn_msPOVM
statement: formalized
proof: formalized
---

# Win implications

Let $\mathscr{S} = (|\psi\rangle, M)$ be a POVM strategy succeeding with probability at least $1 - \varepsilon$ in the Pauli basis test $\mathfrak{G}^\textsc{Pauli}_\mathsf{qldparams}$ of Definition [Pauli basis test](../part-01/def-qld-game.md), $M$ standing for either player's measurements. Let $\gamma(\omega)$ be as in Lemma [Anticommuting question tuples](fact-omega-anticomm-prob.md), write $g_h$ for the low-degree encoding of Definition [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md), and let every average below be over the verifier's content, each content carrying the same weight, restricted where indicated to the contents whose tuple $\omega$ is commuting ($\gamma(\omega) = 0$) or anticommuting ($\gamma(\omega) \neq 0$). Then, with $\simeq_\delta$ the cross-party distance of Definition [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md):

1. (**Consistency**) for every question type $t$, $M^{t,x}_a \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{t,x}_a$;

2. (**Low degree**) for each $W \in \{X, Z\}$ and each of the two line types, the line answer evaluated at the sampled point agrees with the point answer: $M^{(\mathtt{Point}, W), u_W}_a \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{(\mathtt{Line}, W), \ell}_{[\,f(t) = a\,]}$, where $f$ is the polynomial answered and $t$ the parameter of $u_W$ on the line $\ell$;

3. (**Pauli basis consistency**) for each $W$, $M^{(\mathtt{Point}, W), u_W}_a \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{(\textsc{Pauli}, W)}_{[g_h(u_W) = a]}$;

4. (**Commutation**) for each $W$, on average over *commuting* $\omega$, $M^{(\mathtt{Pair}, W), \omega}_b \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{\mathtt{Pair}, \omega}_{[\beta_W = b]}$;

5. (**Commutation consistency**) for each $W$, on average over commuting $\omega$, $M^{(\mathtt{Point}, W), u_W}_{[\operatorname{tr}(\cdot\, r_W) = b]} \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{(\mathtt{Pair}, W), \omega}_b$;

6. (**Magic square**) on average over *anticommuting* $\omega$, the $\mathtt{Constraint}$ and $\mathtt{Variable}$ measurements at $\omega$ form a strategy for the Magic Square game of value $1 - O(\varepsilon)$; consequently, if the first player's measurements are projective, Lemma [Direct Magic Square anticommutation — what the pipeline actually needs](../part-01/lem-ms-direct-anticomm.md) gives, for the second player's $\pm 1$-observables $B^{\mathtt{Variable}_j, \omega}$,

    $$
    \mathop{\mathbb{E}}_{\omega \,:\, \gamma(\omega) \neq 0}
    \left\| {\bigl({I} \otimes \{B^{\mathtt{Variable}_1, \omega},
    B^{\mathtt{Variable}_5, \omega}\}\bigr) |\psi\rangle} \right\|^2 \;\leq\; 16049664\,\varepsilon\;;
    $$

7. (**Magic square consistency**) on average over anticommuting $\omega$, $M^{(\mathtt{Point}, X), u_X}_{[\operatorname{tr}(\cdot\, r_X) = b]} \otimes {I} \simeq_{172\varepsilon} {I} \otimes M^{\mathtt{Variable}_1, \omega}_b$, and the same with $Z$, $r_Z$ and $\mathtt{Variable}_5$.

The Lean proves it for a strategy in any bipartite model (Definition [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)) — a unit state and, for each player, a family of POVMs in that player's algebra — items 1–5 and 7 for any such families and item 6 with the first player's measurements projective; the statement above is its tensor-product instance.

## Depends on

- [Pauli basis test](../part-01/def-qld-game.md)
- [Anticommuting question tuples](fact-omega-anticomm-prob.md)
- [Direct Magic Square anticommutation — what the pipeline actually needs](../part-01/lem-ms-direct-anticomm.md)
- [The Magic Square](../../foundations/part-01/def-magic-square.md)
- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)
- [Seeded CL low individual degree test](../part-01/def-lidt-cl.md)

## Proof

Items 1–5 and 7 are one lemma applied seven times. The question distribution factors as an ordered type edge times the content, both uniform, so a question pair arising from a fixed edge of the type graph carries at least $1/86$ of the mass — $86$ being the ordered pairs counted in Definition [Pauli basis test](../part-01/def-qld-game.md) — and the conditional failure of any subtest is therefore at most $86\varepsilon$. Each rule of $\mathcal{D}^\textsc{Pauli}$ accepts only when two named readings of the two answers agree, so [(1)](../../foundations/part-02/def-cross-distance.md) converts that into $172\varepsilon$ of cross-party distance for the measurements coarse-grained along those readings. The four rules gated on $\gamma$ check nothing on the other value of $\gamma$, which is why their averages are restricted.

Item 6 is not of that shape. Relabelling the $\mathtt{Constraint}_i$ and $\mathtt{Variable}_j$ answers at a fixed $\omega$ into the Magic Square game's alphabet — the three bits placed at the constraint's cells, the bit passed through — gives a strategy for $\mathfrak{G}^\mathrm{MS}$, and relabelling outcomes is data processing, so that strategy wins whenever the Pauli test's own rule would have accepted. Its failure is therefore at most the Magic Square game's own question-weighted sum of the Pauli test's conditional failures at the corresponding question pairs, which is $86\varepsilon$ on average over anticommuting $\omega$ — one factor of $86$ and not thirty-six, because $\mathfrak{G}^\mathrm{MS}$'s distribution is itself normalized. The conditional strategy's constraint measurements are coarse-grainings of the first player's, hence projective when those are, and Lemma [Direct Magic Square anticommutation — what the pipeline actually needs](../part-01/lem-ms-direct-anticomm.md) applied to each conditional strategy and averaged gives $186624 \cdot 86 = 16049664$. This uses the strategy's own observables and invokes no Magic Square rigidity.

## Lean

Formalized as [`MIPRE.QLD.subtest_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.subtest_le), [`MIPRE.QLD.agree_subtest_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.agree_subtest_le), [`MIPRE.QLD.item_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_consistency), [`MIPRE.QLD.item_lowDeg_aline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_lowDeg_aline), [`MIPRE.QLD.item_lowDeg_dline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_lowDeg_dline), [`MIPRE.QLD.item_pauli_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_pauli_consistency), [`MIPRE.QLD.item_commutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_commutation), [`MIPRE.QLD.item_commutation_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_commutation_consistency), [`MIPRE.QLD.item_ms_consistency_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_ms_consistency_X), [`MIPRE.QLD.item_ms_consistency_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_ms_consistency_Z), [`MIPRE.QLD.msPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.msPOVM), [`MIPRE.QLD.msEps`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.msEps), [`MIPRE.QLD.condFail_ms_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.condFail_ms_le), [`MIPRE.QLD.one_sub_povmValue_ms_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.one_sub_povmValue_ms_le), [`MIPRE.QLD.sum_msEps_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_msEps_le), [`MIPRE.QLD.item_magicSquare`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.item_magicSquare), [`MIPRE.QLD.isPVMIn_msPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVMIn_msPOVM).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2161](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2161)
