---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.TypeBranch, Cslib.SessionTypes.Endpoint.TypeLabel, Cslib.SessionTypes.Endpoint.TypeEdge, Cslib.SessionTypes.Endpoint.protocolTree, Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv, Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.refl, Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.symm, Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.trans
statement: formalized
proof: formalized
---

# Session typing up to protocol equivalence

142 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/index.html).

## Payload and continuation branches of an endpoint action

The two distinct children of an endpoint action.

Formalized by `Cslib.SessionTypes.Endpoint.TypeBranch`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#type-branch).

## Labels of observable protocol-tree edges

Observable guarded tree edges. Endpoint metadata is never erased.

Formalized by `Cslib.SessionTypes.Endpoint.TypeLabel`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#type-label).

## Visible edge of a protocol tree after root unfolding

One visible tree edge obtained by the existing guarded root unfolding.

Formalized by `Cslib.SessionTypes.Endpoint.TypeEdge`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#type-edge).

## Labelled transition system of protocol-tree observations

Canonical CSLib LTS instance for guarded type-tree observations only.

Formalized by `Cslib.SessionTypes.Endpoint.protocolTree`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#protocol-tree).

## Regular-tree equivalence of protocols as bisimilarity

Equirecursive regular-tree equality is canonical strong bisimilarity,
not equality of graph codes, cursors or finite constructor syntax.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#tree-equiv).

## Protocol tree equivalence is reflexive

Reflexivity comes from the canonical CSLib bisimilarity API.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.refl`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#refl).

## Protocol tree equivalence is symmetric

Symmetry comes from the canonical CSLib bisimilarity API.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.symm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#symm).

## Protocol tree equivalence is transitive

Transitivity comes from composition of canonical CSLib bisimulations.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.trans`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#trans).

## Root unfolding preserves protocol-tree edges

Root unfolding exposes exactly the same observation edges.

Formalized by `Cslib.SessionTypes.Endpoint.typeEdge_unfold`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#type-edge-unfold).

## A protocol is tree-equivalent to its unfolding

One unfolding is semantically equivalent even though its code changes.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_unfold`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#tree-equiv-unfold).

## Head and branch matching of protocols up to a child relation

Exact head and branch correspondence for a relation on child trees.
Payload and continuation are related separately; only metadata is literal.

Formalized by `Cslib.SessionTypes.Endpoint.HeadMatch`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#head-match).

## Head matching is monotone in the child relation

Head matching is monotone in the child relation.

Formalized by `Cslib.SessionTypes.Endpoint.HeadMatch.mono`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#mono).

## Head-matching relations are bisimulations

A relation matching literal unfolded heads and both child branches is a
canonical CSLib bisimulation. This is the coinductive proof rule, not an axiom.

Formalized by `Cslib.SessionTypes.Endpoint.headMatch_isBisimulation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#head-match-is-bisimulation).

## Tree-equivalent protocols have matching heads

Canonical bisimilarity determines literal head metadata and both
semantically equivalent child branches. No graph-code equality is required.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#head).

## Coinduction principle for protocol tree equivalence

Coinduction on an explicitly supplied tree relation, checked by CSLib.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.coind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#coind).

## Characterization of tree equivalence by matching heads

Exact semantic root/branch characterization, in BOTH directions.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_iff_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#tree-equiv-iff-head).

## Unfolding both protocols preserves and reflects tree equivalence

Unfolding on either or both sides leaves the regular tree unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_unfold_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#tree-equiv-unfold-iff).

## Tree equivalence is a congruence for name sending

Constructor congruence matches same-direction name continuations.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.sendName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#send-name).

## Tree equivalence is a congruence for name receiving

Constructor congruence also matches input direction separately.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.recvName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#recv-name).

## Tree equivalence is a congruence for endpoint sending

Payload and continuation congruence do not conflate the two branches.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.sendEndpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-01/index.html#send-endpoint).

## Tree equivalence is a congruence for endpoint receiving

Endpoint receive congruence preserves literal role/rank metadata.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.recvEndpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#recv-endpoint).

## Head matching transfers to dual protocols

Dualizing a head changes subject direction and continuation orientation,
but leaves payload orientation and role/rank metadata untouched.

Formalized by `Cslib.SessionTypes.Endpoint.HeadMatch.dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#dual).

## Duality preserves protocol tree equivalence

Semantic equivalence is preserved by actual protocol duality, including
recursive payloads with independently chosen orientation.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#dual-2).

## Duality preserves and reflects protocol tree equivalence

Duality both preserves and reflects equivalence, not only one direction.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_dual_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#tree-equiv-dual-iff).

## Protocol tree equivalence is an equivalence relation

The semantic type relation is a genuine equivalence relation.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_equivalence`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#tree-equiv-equivalence).

## Tree equivalence of endpoint sends, componentwise

Exact endpoint-send characterization exposes literal metadata equality
and separate semantic payload/continuation equivalences for conversion.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_sendEndpoint_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#tree-equiv-send-endpoint-iff).

## Tree equivalence of endpoint receives, componentwise

Receive characterization preserves the same independent payload metadata.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.treeEquiv_recvEndpoint_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#tree-equiv-recv-endpoint-iff).

## Tree equivalence preserves completion of a protocol

Activity/completion is invariant under semantic type equivalence.

Formalized by `Cslib.SessionTypes.Endpoint.Protocol.TreeEquiv.done_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/TypeEquivalence.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#done-iff).

## Equivalence of endpoint capabilities

Capability equivalence explicitly retains the enclosing capability rank,
which is not an observation of Protocol.TreeEquiv.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.Equivalent`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#equivalent).

## Reflexivity of capability equivalence

Reflexivity retains rank and the exact protocol tree.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.Equivalent.refl`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#refl).

## Symmetry of capability equivalence

Symmetry preserves the separately required rank equality.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.Equivalent.symm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#symm).

## Transitivity of capability equivalence

Transitivity composes rank equality and regular-tree equivalence.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.Equivalent.trans`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#trans).

## Duality preserves capability equivalence

Duality retains the separate rank and preserves protocol-tree equivalence.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.Equivalent.dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#dual-3).

## Semantic peer compatibility of an ownership map

Semantic peer compatibility keeps actual capability ranks equal and
compares dual protocol trees, not merely their direction or payload metadata.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Compatible`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#compatible).

## Syntactic compatibility implies semantic compatibility

Old syntactic peer compatibility implies the semantic condition.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.compatible_of_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#compatible-of-raw).

## Conversion-enabled endpoint typing judgement

Seven syntax-directed rules. No readiness, Step, retyping, preservation
or consistent raw representative is a typing premise. Endpoint input installs
its actual advertised code; endpoint output transfers the actual owned slot.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#has-type).

## Base endpoint typing embeds into conversion typing

Actual seven-rule induction embeds the raw judgement. This does not
transport the raw judgement's substitution or progress theorem to new terms.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.of_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#of-raw).

## Output typing at a code equivalent to one send then end

Local finite-tail conversion: replacing a one-send-then-end protocol by
an equivalent code yields a usable output subject, retaining its actual next
code and rank. This is not arbitrary context retyping.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.one_action_tail`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#one-action-tail).

## Output inversion for conversion typing

Conversion output inversion exposes actual owned payload metadata and
semantic comparison, never a supplied retyping result.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.out_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTyping.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#out-inv).

## Conversion-typed processes are well scoped

Canonical scope follows from the seven conversion rules.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-02/index.html#closed-at).

## Conversion-typed processes have no sum or replication

Typing excludes sum and repl by syntax, not by a caller fragment premise.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.finiteLinear`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#finite-linear).

## Parallel inversion for conversion typing

Parallel inversion derives its actual disjoint map split.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#par-inv).

## Restriction inversion for conversion typing

The private pair comes from the actual restriction derivation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nu_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#nu-inv).

## Nil inversion for conversion typing

Nil exposes actual completed ownership and key scope.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nil_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#nil-inv).

## Typed nil admits a completed scoped capability

Only a scoped actually completed capability can be added at nil.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nil_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionInversion.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#nil-insert).

## Weakening conversion typing by a completed capability

An unused completed endpoint may be added through every current typing
constructor. Scope and freshness are explicit; active weakening is not admitted.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.weaken_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#weaken-completed).

## Weakening conversion typing by a disjoint completed context

A disjoint completed context can be reattached to any typed process,
with the exact finite-map union required by parallel-nil congruence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.weaken_completed_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#weaken-completed-union).

## Removing a parallel nil preserves conversion typing

Removing a parallel nil reattaches exactly its completed ownership;
no active capability is silently dropped.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#par-nil-elim).

## Erasing a role with an absent name preserves typing

A role can be erased when its physical name is absent from every
subject, payload and binder-adjusted continuation position of the typed term.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.erase_nameAbsent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#erase-name-absent).

## Owned capabilities with absent names are completed

An owned capability with no physical-name occurrence must already be
completed. This is derived from typing, including endpoint payload positions.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.absent_lookup_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionResources.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#absent-lookup-completed).

## Retyping along ownership-map equivalence

GENERAL arbitrary-depth, arbitrary-context retyping, by all seven typing
constructors. Target ownership, ranks and every unfolded branch are derived.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionRetyping.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionRetyping.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#retype).

## Ownership-map equivalence preserves typing in both directions

Equivalence transports typing in BOTH directions at the same process/depth.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.retype_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionRetyping.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionRetyping.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#retype-iff).

## Collision-free renaming preserves conversion typing

GENERAL name transport with collision freedom on actual owned keys and
canonical ambient name scope; protocol codes, roles and ranks stay exact.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#rename).

## Lifting past a binder preserves conversion typing

Lift uses the canonical cutoff-aware name and process operations.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#lift).

## Swapping adjacent binders preserves conversion typing

Swap retains roles, protocols and ranks while permuting two ambient binders.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionTransport.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#swap).

## Endpoint substitution preserves conversion typing

GENERAL endpoint substitution: retain the ACTUAL transmitted capability's
code and rank at the sent polarized key, allowing its opposite-role alias.
Collision freedom is needed only for that exact key and canonical substitution.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subst_endpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#subst-endpoint).

## Endpoint substitution with freshness from a disjoint split

GENERAL split-derived freshness: actual payload ownership and the
receiver's already-owned carrier derive non-aliasing even after advancement.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subst_endpoint_from_split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#subst-endpoint-from-split).

## Passive name substitution preserves conversion typing

GENERAL passive substitution transports all scoped positions but adds
NO capability. The input context contains only lifted outer ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subst_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionSubstitution.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#subst-passive).

## Communicating subjects have semantically dual capabilities

At a semantically compatible combined interface, actual disjoint same-name
ownership derives opposite roles, literal cap-rank agreement and semantic
duality, not raw capability equality.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.communicating_equivalent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#communicating-equivalent).

## Peer of a passive send head has an equivalent receive head

Semantic duality forces an actual receive-name head and equivalent tail,
while keeping the receiver's literal continuation code.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.passive_peer_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-03/index.html#passive-peer-head).

## Peer of an endpoint send head has an equivalent receive head

Endpoint peer heads preserve literal advertised role/rank, independently
equivalent payload and continuation branches, and payload orientation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.endpoint_peer_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#endpoint-peer-head).

## Input inversion for conversion typing

Input inversion retains its actual advertised code and typed continuation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.inp_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#inp-inv).

## Passive head communication preserves conversion typing

GENERAL passive communicating-head preservation at a semantically
compatible actual split, with literal receiver-tail and rank evidence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.passive_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#passive-head-preservation).

## Endpoint delegation preserves conversion typing

At an initially semantically compatible disjoint split, endpoint head
communication transfers EXACT v, retaining the receiver's separately equivalent
advertised payload/tail codes.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.endpoint_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#endpoint-head-preservation).

## Head update leaves other lookups unchanged

Exact two-insert head updates leave every other actual lookup unchanged,
without requiring the receiver-tail code to equal the sender's dual.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.head_update_other`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#head-update-other).

## Head communication preserves conversion typing

A typed opposite-head pair at an initially semantically compatible interface
yields packed literal-head preservation. Both actual heads and payload/tail
correspondence are conclusions, not fields in a protocol or admission predicate.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#head-preservation).

## Head update leaves the transmitted payload slot unchanged

A transmitted payload slot is literally unchanged in the combined map;
its peer role may coexist, but it is neither carrier update key.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.endpoint_payload_after`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCommunication.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#endpoint-payload-after).

## Lowering a lifted process preserves conversion typing

Canonical lowering removes only actual outer lifted keys, preserving
all conversion typing without a closed-hole restriction.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.unlift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#unlift).

## Forward scope extrusion preserves conversion typing

The forward canonical scope rule preserves the exact external context
and ambient depth, with the dual pair derived from restriction typing.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.scope_forward`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#scope-forward).

## Adding a role unused by the partner preserves conversion typing

A role missing from one component can be reattached only after actual
absence in its typed partner derives completion of the advertised capability.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.insert_from_absent_partner`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#insert-from-absent-partner).

## Restoring the bound pair to the restricted component

In the actual scope split, either freshly bound role can be moved
back to the restricted component only when partner absence proves it completed.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.restore_scope_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#restore-scope-pair).

## Reverse scope extrusion preserves conversion typing

Reverse scope transport recovers the exact external ownership split
from the actual restriction/parallel typing, with no closed-hole premise.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.scope_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#scope-reverse).

## Scope extrusion preserves conversion typing in both directions

Both directions of the canonical scope congruence preserve exact
external polarized ownership and the unchanged ambient binder depth.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.scope_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionScope.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#scope-iff).

## Parallel commutation preserves conversion typing

Parallel commutation swaps a derived disjoint split, not its capabilities.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_comm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#par-comm).

## Parallel reassociation preserves conversion typing

Parallel reassociation preserves the actual three-way disjoint split.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_assoc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#par-assoc).

## Reverse parallel reassociation preserves conversion typing

Reverse reassociation recovers both sub-splits from the supplied typing.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_assoc_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#par-assoc-reverse).

## Adding a parallel nil preserves conversion typing

Adding a parallel nil allocates it no ownership; no active slot is dropped.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.par_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#par-nil-intro).

## Removing a restriction around nil preserves conversion typing

Restriction of nil has exactly the completed external ownership of nil.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nu_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#nu-nil-elim).

## Adding a restriction around nil preserves conversion typing

A completed fresh pair may be introduced around nil while retaining
all original external capabilities and scope.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nu_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#nu-nil-intro).

## Swapping nested restrictions preserves conversion typing

Nested restriction commutation swaps their derived complete dual pairs.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nu_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-04/index.html#nu-swap).

## Reverse restriction swap preserves conversion typing

Reverse nested restriction commutation uses the canonical involution.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.nu_swap_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#nu-swap-reverse).

## Structural congruence preserves conversion typing

Every existing canonical structural congruence preserves endpoint typing
in both directions with exactly the same depth and ownership. Unsupported
choice/replication shapes are rejected by the typing-derived finite invariant.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionCong.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#cong-iff).

## Subject reduction at a compatible conversion interface

From a typed source at an initially compatible interface, all five
canonical reduction constructors preserve typing and compatibility, with one
matched external subject-pair advancement or an unchanged interface when
communication is private. No fragment or enabled-edge premise is required.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subject_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#subject-reduction).

## Subject reduction at a balanced interface

A typed source with a balanced initial interface retains typing and balance
after any canonical step. Balance supplies the required compatibility; the
exact zero-or-one external advancement evidence is retained.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subject_reduction_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#subject-reduction-balanced).

## Subject reduction at the empty interface

An empty-interface typed network retains empty-interface typing through
any canonical step. The empty context is balanced, hence compatible, including
communication behind restrictions and pre/post congruence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.subject_reduction_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#subject-reduction-empty).

## Typing and compatibility persist along finite executions

A typed source at an initially semantically compatible interface retains
typing and compatibility through finite actual execution, with a finite trace
of faithful advances. This is safety, not progress or termination.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#reachable).

## Empty-interface typing persists along finite executions

Every finite reachable closed state retains the exact empty interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.reachable_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ConversionReduction.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#reachable-empty).

## Priority-ranked conversion typing judgement

Linear ownership typing with a strict priority check at every guard.
There is no reduction, enabled-edge, progress or preservation field.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#ranked-type).

## Forgetting priorities yields conversion typing

Forgetting guard priorities derives the existing conversion judgement.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.hasType`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#has-type).

## Ranked typing embeds into conversion ranked typing

Explicit seven-case raw-ranked embedding, not theorem-value inheritance.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.of_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#of-raw).

## Parallel inversion for conversion ranked typing

Ranked parallel typing exposes its actual disjoint ownership split.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#par-inv).

## Restriction inversion for conversion ranked typing

Restriction chooses an actual literal-dual pair.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nu_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#nu-inv).

## Nil typing lifts to conversion ranked typing

Nil adds no priority premise beyond actual completed and scoped ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nil_of_hasType`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTyping.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#nil-of-has-type).

## Conversion-ranked output subjects are active

Literal output is active and checks every other owned active key.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.out_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#out-active).

## Conversion-ranked input subjects are active

Literal input is active before either payload kind is received.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.inp_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#inp-active).

## Minimum active role is the subject of a conversion frontier leaf

A minimum active role is exposed as the EXACT subject of an actual leaf.
The disjoint ownership split and canonical rearrangement are DERIVED outputs;
no ready guard or normalizing typing result is required from the caller.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.GuardFrontier.expose_minimum`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#expose-minimum).

## Completed conversion-ranked frontiers are congruent to nil

A frontier with no active ownership cannot contain a live prefix.
Completion is the PROCESS congruence to nil, not a completed empty interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.GuardFrontier.completed_nil`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#completed-nil).

## Minimum guard leaf cannot own an equivalent dual peer

A semantic equal-rank active peer cannot inhabit the selected minimum guard.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.minimum_peer_separate`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionFrontier.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#minimum-peer-separate).

## Weakening conversion ranked typing by a completed capability

Adding a fresh completed capability preserves every guard inequality
through all seven rules. No active capability can be added by this theorem.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.weaken_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#weaken-completed).

## Erasing a key whose name is absent preserves conversion ranked typing

Actual all-position physical-name absence permits erasure in the
refinement too. Subject and payload lookup obligations are never discarded.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.erase_nameAbsent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-05/index.html#erase-name-absent).

## Weakening conversion ranked typing by a disjoint completed context

Reattaching a disjoint completed finite context preserves all guards.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.weaken_completed_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionResources.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#weaken-completed-union).

## Equivalent contexts preserve the guard condition

Same domains, literal cap ranks and actual done equivalence preserve GuardMin.

Formalized by `Cslib.SessionTypes.Endpoint.GuardMin.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#retype).

## Equivalent contexts preserve conversion ranked typing

GENERAL arbitrary-depth, arbitrary-context retyping, by all seven typing
constructors. Target ownership, ranks and every unfolded branch are derived.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#retype-2).

## Context equivalence transports conversion ranked typing both ways

Equivalence transports typing in BOTH directions at the same process/depth.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.retype_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionRetyping.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#retype-iff).

## Collision-free renaming preserves conversion ranked typing

GENERAL name transport with collision freedom on actual owned keys and
canonical ambient name scope; protocol codes, roles and ranks stay exact.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#rename).

## Binder lifting preserves conversion ranked typing

Lift uses the canonical cutoff-aware name and process operations.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#lift).

## Binder swap preserves conversion ranked typing

Swap retains roles, protocols and ranks while permuting two ambient binders.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionTransport.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#swap).

## Endpoint substitution preserves conversion ranked typing

GENERAL endpoint substitution: retain the ACTUAL transmitted capability's
code and rank at the sent polarized key, allowing its opposite-role alias.
Collision freedom is needed only for that exact key and canonical substitution.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subst_endpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#subst-endpoint).

## Split-derived freshness for conversion endpoint substitution

GENERAL split-derived freshness: actual payload ownership and the
receiver's already-owned carrier derive non-aliasing even after advancement.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subst_endpoint_from_split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#subst-endpoint-from-split).

## Passive substitution preserves conversion ranked typing

GENERAL passive substitution transports all scoped positions but adds
NO capability. The input context contains only lifted outer ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subst_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionSubstitution.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#subst-passive).

## Inversion of conversion-ranked input typing

Input inversion retains its actual advertised code and typed continuation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.inp_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#inp-inv).

## Passive head communication preserves conversion ranked typing

GENERAL passive communicating-head preservation at a semantically
compatible actual split, with literal receiver-tail and rank evidence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.ranked_passive_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#ranked-passive-head-preservation).

## Endpoint head communication preserves conversion ranked typing

At an initially semantically compatible disjoint split, endpoint head
communication transfers EXACT v, retaining the receiver's separately equivalent
advertised payload/tail codes.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.ranked_endpoint_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#ranked-endpoint-head-preservation).

## Head preservation for a conversion-ranked opposite pair

A typed opposite-head pair at an initially semantically compatible interface
yields packed literal-head preservation. Both actual heads and payload/tail
correspondence are conclusions, not fields in a protocol or admission predicate.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#head-preservation).

## Conversion head communication yields a semantic advance

For a ranked-typed opposite-head pair at an initially semantically compatible
interface, head preservation constructs a faithful semantic advance and a
compatible ranked residual.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.head_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCommunication.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#head-advance).

## Same-name conversion guards are opposite and communicate

For disjoint ranked-typed same-name leaves at a semantically compatible
combined interface, literal guard shapes have opposite directions and yield
an actual canonical Step.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.same_name_guards_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionProgress.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionProgress.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#same-name-guards-step).

## Progress for semantically balanced conversion frontiers

GENERAL balanced ranked frontier progress. A minimum over ALL active
owned roles exposes two distinct opposite subject leaves, from which actual
canonical communication follows. Completion is process-level Cong to nil.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.GuardFrontier.progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionProgress.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionProgress.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#progress).

## Conversion ranked typing descends from a lifted process

Reflection of an actual lifted term recovers every priority and context entry.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.unlift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#unlift).

## Forward scope extrusion preserves conversion ranked typing

Extrusion lifts the partner's real ownership while retaining every guard.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.scope_forward`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#scope-forward).

## Adding a role unused by the partner preserves conversion ranked typing

Moving a partner-owned role back requires actual absence to DERIVE
completion from conversion typing before refined completed weakening is applied.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.insert_from_absent_partner`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-06/index.html#insert-from-absent-partner).

## Restoring the bound pair preserves conversion ranked typing

Restoring the bound pair adds only absent completed partner roles; all
original active ownership and inequalities of the restricted component remain.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.restore_scope_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#restore-scope-pair).

## Reverse scope extrusion preserves conversion ranked typing

Reverse extrusion derives the entire outer ownership split from typing,
removes only genuinely absent partner roles and retains all guard inequalities.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.scope_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#scope-reverse).

## Conversion ranked typing is invariant under scope extrusion

Exact bidirectional canonical scope transport for the same refinement.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.scope_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionScope.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#scope-iff).

## Parallel commutation preserves conversion ranked typing

Commutation retains the actual disjoint split and both ranked subterms.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_comm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#par-comm).

## Parallel reassociation preserves conversion ranked typing

Reassociation derives all pairwise disjointness from actual typing.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_assoc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#par-assoc).

## Reverse parallel reassociation preserves conversion ranked typing

Reverse reassociation retains exact contexts and guard checks.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_assoc_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#par-assoc-reverse).

## Removing a parallel nil preserves conversion ranked typing

Nil's actual completed ownership can be reattached without new dependencies.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#par-nil-elim).

## Adding a parallel nil preserves conversion ranked typing

Nil introduction allocates an empty ownership context, not an active frame.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.par_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#par-nil-intro).

## Removing a restriction around nil preserves conversion ranked typing

Restricting nil is equivalent to its original completed/scoped interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nu_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#nu-nil-elim).

## Restricting nil preserves conversion ranked typing

A completed fresh pair can be introduced around nil without changing guards.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nu_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#nu-nil-intro).

## Swapping two restrictions preserves conversion ranked typing

Swapping the two restrictions preserves all guard constraints by the
GENERAL capture-safe rename theorem and the exact four-role context equation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nu_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#nu-swap).

## Reverse restriction swap preserves conversion ranked typing

Reverse restriction swap uses the canonical process involution.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.nu_swap_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#nu-swap-reverse).

## Structural congruence preserves conversion ranked typing

Every canonical Cong constructor preserves the whole priority refinement
at exactly the same context and ambient depth. Unsupported sum/replication
constructors are impossible by the invariant DERIVED from refinement typing.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionCong.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#cong-iff).

## Conversion ranked subject reduction at compatible interfaces

From a typed source at an initially compatible interface, all five
canonical reduction constructors preserve typing and compatibility, with one
matched external subject-pair advancement or an unchanged interface when
communication is private. No fragment or enabled-edge premise is required.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subject_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#subject-reduction).

## Conversion ranked subject reduction at balanced interfaces

A typed source with a balanced initial interface retains typing and balance
after any canonical step. Balance supplies the required compatibility; the
exact zero-or-one external advancement evidence is retained.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subject_reduction_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#subject-reduction-balanced).

## Conversion ranked subject reduction at the empty interface

An empty-interface typed network retains empty-interface typing through
any canonical step. The empty context is balanced, hence compatible, including
communication behind restrictions and pre/post congruence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.subject_reduction_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#subject-reduction-empty).

## Finite runs keep conversion ranked typing at compatible interfaces

A ranked-typed source at an initially semantically compatible interface
retains typing and compatibility through finite actual execution, with a finite
trace of faithful advances. This is safety, not progress or termination.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#reachable).

## Reachable closed conversion-ranked states keep the empty interface

Every finite reachable closed state retains the exact empty interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.reachable_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionReduction.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#reachable-empty).

## Conversion-ranked processes have a typed frontier normal form

Normalization is derived from finite syntax, then NEW ranked Cong keeps ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.frontier_normal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#frontier-normal).

## Global progress of conversion-ranked processes at balanced interfaces

For a ranked-typed process at ANY balanced interface, global progress
holds, including disconnected networks.
All private channels are tracked through the derived restriction tower.
Completion means process congruence to nil, not completion of the interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.progress_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-07/index.html#progress-balanced).

## Closed conversion-ranked networks are completed or can step

A closed finite ranked network is completed or takes an ACTUAL canonical
step. Ambient passive-name depth is arbitrary; no readiness witness is supplied.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.progress_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-08/index.html#progress-empty).

## Progress at reachable states of closed conversion-ranked networks

Global progress holds at every finite reachable state of a closed ranked
network. No fairness, eventual liveness or recursive termination is asserted.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.RankedType.reachable_progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RankedConversionGlobal.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/part-08/index.html#reachable-progress).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Session typing up to protocol equivalence](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/session-typing-up-to-protocol-equivalence)
