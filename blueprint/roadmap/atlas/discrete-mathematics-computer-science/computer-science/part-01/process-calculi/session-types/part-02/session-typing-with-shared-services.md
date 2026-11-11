---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Runtime.ServiceSignature, Cslib.SessionTypes.Endpoint.Runtime.ServiceEnv, Cslib.SessionTypes.Endpoint.Runtime.Separated, Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority, Cslib.SessionTypes.Endpoint.Runtime.separated_empty, Cslib.SessionTypes.Endpoint.Runtime.separated_singleton, Cslib.SessionTypes.Endpoint.Runtime.invocation_priority_singleton, Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate
statement: formalized
proof: formalized
---

# Session typing with shared services

133 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/index.html).

## Shared service signature

Shared permission describes a transferred endpoint, not owned linear state.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceSignature`, a structure declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#service-signature).

## Shared service environment

Constant-only shared names use the existing Finmap, not a new name foundation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceEnv`, an abbreviation declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#service-env).

## Separation of owned linear names from shared names

An owned linear endpoint is never a declared shared trigger's physical name.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#separated).

## Priority of a shared invocation over active owned keys

Shared invocation precedes every actual active owned LINEAR key; none exempt.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#invocation-priority).

## Empty ownership is separated from shared names

Empty captured ownership has no linear/shared alias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.separated_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#separated-empty).

## Singleton context with a nonshared name is separated

A singleton received/actual endpoint is separate exactly at its own name.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.separated_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#separated-singleton).

## Invocation priority for a singleton of rank above the priority

Singleton invocation still compares the ACTIVE payload's actual cap rank.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.invocation_priority_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironment.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#invocation-priority-singleton).

## Structural shared-service template

A template is a structural tree of declared shared inputs, never active outputs.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#service-template).

## Service templates are invariant under lifting

Canonical lifting preserves literal shared constants through every structural wrapper.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.lift_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#lift-iff).

## Service templates are invariant under binder swapping

Canonical swap preserves template guards, including wrappers under nested binders.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.swap_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#swap-iff).

## Service templates are invariant under structural congruence

ALL16 canonical Cong constructors preserve structural guarded templates in BOTH directions.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#cong-iff).

## Unguarded shared input on a given name

Actual unguarded shared input presence through structural wrappers; input stops here.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.AcceptIn`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#accept-in).

## Structural congruence preserves unguarded shared inputs

All canonical congruences preserve actual shared-input presence, not execution.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.accept_cong`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#accept-cong).

## Persistent service offer on a given name

Persistent services expose input leaves within actual replicated structural templates.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.OfferedIn`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#offered-in).

## Offered services have an unguarded shared input

Every persistent offered service has an actual unguarded input leaf.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.offered_accept`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#offered-accept).

## Structural congruence preserves persistent service offers

ALL16 actual Cong rules preserve persistent service offering, including wrappers
inside replication and actual replica unfolding. No closure constructor is used.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.offered_cong`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#offered-cong).

## Declared persistent service offer

Declared signature plus actual persistent guarded service syntax, never execution data.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Offered`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#offered).

## Idle process as a structural service template

Quiescent structural service templates include waiting declared inputs and wrappers.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Idle`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#idle).

## Declared service offers are invariant under congruence

All canonical Cong constructors preserve each actual declared persistent offer.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Offered.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#cong-iff-2).

## Idleness is invariant under structural congruence

Idle is precisely structural guarded-template quiescence and is Cong-invariant.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Idle.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ServiceTemplates.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-01/index.html#cong-iff-3).

## Name map fixing every declared shared constant

A name map leaves every declared shared constant literally fixed.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.FixesShared`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#fixes-shared).

## Nonaliasing of owned-name images with shared constants

Actual owned-key images cannot alias a declared shared physical name.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#non-aliases).

## Binder extension preserves fixing of shared constants

Binder extension still fixes shared constants, which are unchanged by lifting.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.FixesShared.under`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#under).

## Rekeying along a nonaliasing name map yields separation

The actual target ownership rekey has static name separation, not a desired type result.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.separated`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#separated-2).

## Erasing an owned key preserves nonaliasing

Erasure restricts the actual owned domain and cannot add a name-map alias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#erase).

## Updating an already-owned key preserves nonaliasing

Advancing an already-owned key leaves the name-map domain unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#insert-owned).

## Every name map is nonaliasing on empty ownership

Empty BODY ownership imposes no linear-image nonalias obligations.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.nonaliases_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#nonaliases-empty).

## Binder extension preserves nonaliasing of lifted contexts

Binder extension maps lifted owned names to lifted images, never new shared constants.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.under_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#under-lift).

## Nonaliasing survives adding a received parameter under a binder

A newly received parameter remains var0 under the canonical binder map.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.under_received`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#under-received).

## Nonaliasing survives binding a private session pair

Both private-role keys are fresh var0; only actual outer names need nonalias transport.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.under_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#under-bind).

## Nonaliasing restricts to the left part of a union

Actual left-domain restriction of an ownership union preserves map nonalias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.union_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#union-left).

## Nonaliasing restricts to the right part of a union

Actual right-domain restriction likewise preserves map nonalias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.NonAliases.union_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#union-right).

## Service templates are preserved by renamings fixing shared names

Structural templates transport through a declared-constant-fixing name map;
input BODY typing is handled separately, not hidden in this shape predicate.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#rename).

## Rekeying preserves shared invocation priority

Rekeying retains actual cap values and therefore shared-priority comparisons.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority.rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#rekey).

## Rekeying the empty context gives the empty context

An empty owned context stays empty under the canonical context rekey operation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.rekey_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#rekey-empty).

## Rekeying a singleton moves its key and keeps its capability

Rekeying a singleton moves its actual key and retains its capability verbatim.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.rekey_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#rekey-singleton).

## Separation gives nonaliasing for binder lifting

Canonical binder lifting cannot send a nonshared owned name into the shared namespace.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.nonaliases_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#nonaliases-lift).

## Separation gives nonaliasing for binder swapping

Canonical binder swapping likewise preserves actual owned-name nonalias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.nonaliases_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNames.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#nonaliases-swap).

## Erasing an owned key preserves separation

Erasing an actual owned key cannot create a shared/linear name alias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#erase-2).

## Inserting a nonshared key preserves separation

Inserting a statically nonshared key preserves physical-name separation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-02/index.html#insert).

## Binder lifting preserves separation

Actual binder lifting preserves nonshared physical names: constants cannot
be newly produced by lifting a linear variable.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#lift).

## Binding a private pair preserves separation

A literal private pair has variable names, never declared shared constants.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#bind).

## Separation restricts to the left part of a union

A left child of the actual ownership union retains static shared-name separation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.union_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#union-left).

## Separation restricts to the right part of a disjoint union

Disjointness prevents right-child lookup shadowing by the left ownership domain.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.union_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedEnvironmentTransport.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#union-right).

## Runtime typing with guarded shared replication

Ten syntax-directed rules over canonical Pi, fixed static ranks and actual
ownership. Accept/serve may carry completed ambient annotations, never body capture.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedServices.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedServices.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#has-type).

## Finite ranked typing embeds into runtime typing under separation

Real ALL7-rule induction embeds finite ranked typing, including delegation;
there is no finite-judgement constructor in the new runtime typing.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.of_finite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SharedServices.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/SharedServices.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#of-finite).

## Extension of a shared service environment

Old shared declarations retain their EXACT signature in the larger environment.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.EnvExtends`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#env-extends).

## Service templates survive environment extension

A declared guarded template remains such under literal signature extension.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.env_extend`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#env-extend).

## Environment extension preserves runtime typing under separation

General Γ-extension requires static separation of ALL actual owned names.
The proof establishes fresh lifted/private/received BODY names, rather than
assuming environment monotonicity or carrying a future/result field.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.env_extend`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeEnvironmentWeakening.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#env-extend-2).

## Runtime typing separates owned names from shared services

Completed ambient annotations still obey actual shared/linear name separation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.separated`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#separated).

## Replicated runtime processes have completed ownership

Replication has only COMPLETED ambient ownership, not necessarily empty annotation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.repl_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#repl-completed).

## Typed replication has a body with empty ownership

Replicated BODY ownership is exactly EMPTY, while ambient annotations may be completed.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.repl_body_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#repl-body-empty).

## Runtime-typed processes are scoped at the ambient depth

Every rule derives the EXISTING canonical process-scope predicate, including
fresh service parameters and empty-capture replicated template bodies.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#closed-at).

## Typing rule for a replicated input on a shared name

A literal shared-input replica is an admissible structural template, with
its received BODY at the fresh singleton and replica BODY at EMPTY ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.serve_input`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#serve-input).

## Inversion of runtime typing for the nil process

Nil has only actual completed, scoped, separated ambient ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.nil_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#nil-inv).

## Inversion of runtime typing for parallel composition

Parallel inversion derives the actual disjoint linear split at unchanged Γ.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.par_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#par-inv).

## Inversion of runtime typing for restriction

Restriction inversion exposes a real literal-dual bound pair, not a representative.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.nu_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#nu-inv).

## Output subjects are owned endpoints or declared shared names

Actual output subjects are linear-owned or declared shared constants.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.output_subject`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#output-subject).

## Output on a declared shared name is a service invocation

A declared shared output is necessarily an actual endpoint-transfer invocation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.invoke_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#invoke-inv).

## Inversion of runtime typing for input on a shared name

A declared shared input has completed ambient annotations and EXACT fresh
singleton BODY ownership, not captured ambient capabilities.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.accept_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-03/index.html#accept-inv).

## Inversion of runtime typing for replication

General replica inversion retains completed/scoped/separated AMBIENT annotations
and the structurally guarded BODY typed at EXACT EMPTY ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.repl_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#repl-inv).

## Inversion of runtime typing for a replicated shared input

A literal input template exposes its declared signature and fresh received BODY;
completed ambient annotations are NOT inherited by that BODY.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.service_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#service-inv).

## Typed replicated shared inputs are offered services

Typing-derived actual literal-input offering survives completed ambient annotations.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.service_offered`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeInversion.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#service-offered).

## Inserting a completed entry preserves invocation priority

A completed frame is ignored by shared priority, with NO active-payload exemption.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority.insert_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#insert-completed).

## Weakening runtime typing by one fresh completed entry

ALL10 rules admit a fresh COMPLETED ambient annotation. Its name is scoped
and nonshared; accept/serve BODY ownership is unchanged, never captured.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.weaken_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#weaken-completed).

## Weakening runtime typing by a disjoint completed context

A disjoint completed/scoped/nonshared finite ambient frame can be reattached.
The actual replica/accept BODY is not expanded by those annotations.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.weaken_completed_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#weaken-completed-union).

## Erasing an owned key preserves invocation priority

Removing an owned key preserves the shared priority inequalities on the remainder.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeResources.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#erase).

## Owned names absent from a runtime process are completed

An owned name absent from ALL subject/payload/binder-adjusted positions
already has an actual done unfolding, including in the shared runtime rules.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.absent_lookup_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeAbsence.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeAbsence.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#absent-lookup-completed).

## Erasing a key whose name is absent preserves runtime typing

ALL10 runtime rules support erasure only under real all-position absence.
Accept/serve ambient erasure does NOT alter their exact fresh/empty BODY domains.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.erase_nameAbsent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeAbsence.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeAbsence.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#erase-name-absent).

## Equivalent retyping preserves separation from shared names

Semantic capability changes do not change owned physical names or Γ separation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#retype).

## Equivalent retyping preserves invocation priority

Actual active-payload ranks preserve the strict shared invocation priority.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.InvocationPriority.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#retype-2).

## Runtime typing transfers to an equivalent linear context

ALL10 runtime rules retype at arbitrary equivalent linear contexts, with Γ
UNCHANGED. Actual payload codes, literal cap ranks and empty BODY contexts are retained.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#retype-3).

## Runtime typing is invariant under equivalent linear contexts

Equivalent linear interfaces preserve runtime typing in BOTH directions at
exactly the same shared environment, process and ambient depth.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.retype_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRetyping.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#retype-iff).

## Each owned key of a runtime typing is scoped at ambient depth

Every actual owned key is scoped at the runtime derivation's ambient depth.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.lookup_closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#lookup-closed-at).

## Whole owned context of a runtime typing is scoped at ambient depth

Scope applies to the actual complete owned domain, not only active subjects.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.context_closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#context-closed-at).

## Typed service templates own only completed entries

A typed structurally guarded template owns only completed AMBIENT entries.
Its input and replica BODY proofs remain separate and may use their own formal key.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.template_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#template-completed).

## Typed service templates retype at any well-formed completed context

Structurally guarded typed templates can replace only their COMPLETED ambient
annotations. Fresh input/empty replica BODY proofs are retained unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.template_reannotate`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#template-reannotate).

## Typed service templates retype at empty ownership

Clearing completed template annotations produces the EXACT empty BODY
required by replica admission; this is not unconditional active-resource erasure.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.template_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#template-empty).

## Removing a restriction around nil preserves runtime typing

Removing a nil restriction retains its actual completed/scoped/separated ambient.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.nu_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#nu-nil-elim).

## Adding a restriction around nil preserves runtime typing

Introducing a nil restriction chooses a genuinely completed literal-dual pair.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.nu_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTemplateTyping.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-04/index.html#nu-nil-intro).

## Runtime typing under renamings that fix and avoid shared names

ALL10 runtime derivation rules transport actual names with Γ unchanged.
Shared nonalias is required only on OWNED images, not unrestricted passive names.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#rename).

## Binder lifting preserves runtime typing

Canonical binder lift retains the entire runtime derivation and Γ literally.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#lift).

## Binder swapping preserves runtime typing

Canonical swap permutes actual owned binders without changing Γ or cap metadata.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeTransport.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#swap).

## Nonshared endpoint substitution keeps owned names nonshared

An actual nonshared endpoint replacement keeps every owned substituted image nonshared.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.nonaliases_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#nonaliases-subst).

## Passive substitution creates no owned shared-name alias

Passive var0 is NOT owned: even a shared-constant replacement preserves all
actual lifted owned names and creates no linear shared-name alias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.nonaliases_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#nonaliases-passive).

## Runtime typing under substitution of a transmitted endpoint

Actual transmitted endpoint substitution preserves literal role/rank and raw code.
Shared nonalias of b is a static consequence of ACTUAL sender ownership/separation.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subst_endpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#subst-endpoint).

## Runtime typing under passive name substitution

Passive substitution has NO owned var0 and adds NO capability. A scoped shared
constant can be received as data without becoming a linear/service subject.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subst_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#subst-passive).

## Endpoint substitution with side conditions derived from a split

Real sender ownership and a disjoint receiver carrier derive exact-role
freshness and shared nonalias of the actual transmitted endpoint.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subst_endpoint_from_split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSubstitution.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#subst-endpoint-from-split).

## Runtime typing reflects through binder lifting

Reflection of a canonical lifted term retains exact owned capabilities and Γ.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.unlift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#unlift).

## Runtime typing is preserved by forward scope extrusion

Forward extrusion uses the actual disjoint split and literal bound pair.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.scope_forward`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#scope-forward).

## Runtime typing absorbs a role absent from its parallel partner

Partner ownership may be restored only when actual absence DERIVES completion.
Shared nonalias is obtained from the typed owner, not a new unchecked assumption.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.insert_from_absent_partner`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#insert-from-absent-partner).

## Runtime typing restores both bound roles to the restricted side

Restoring a private pair adds only actually absent completed partner roles.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.restore_scope_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#restore-scope-pair).

## Runtime typing is preserved by reverse scope extrusion

Reverse extrusion derives the exact external split from actual typing and
removes only genuinely absent partner roles. No closed-hole or ready premise.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.scope_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#scope-reverse).

## Runtime typing is invariant under scope extrusion

Exact canonical scope transport preserves SAME Γ, n and Δ in both directions.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.scope_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeScope.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#scope-iff).

## Structural congruence preserves runtime typing

ALL16 canonical Cong rules preserve the whole runtime derivation at exactly
SAME Γ/n/Δ, including guarded replicated templates, completed ambient annotations,
and actual runtime delegation continuations. No typing-up-to-Cong constructor.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCong.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCong.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#cong-iff).

## Guarded frontier of guards and idle service templates

Unguarded frontier atoms are actual guards or existing guarded idle templates.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#guarded-frontier).

## Guarded normal form: restrictions over a guarded frontier

Actual private restriction towers around a guarded runtime frontier.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedNormal`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#guarded-normal).

## Process with no exposed output on a declared shared name

No exposed output is addressed to an actually declared shared constant.
Prefix bodies are not inspected. This is syntax only, not a GLOBAL premise.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.RequestFree`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#request-free).

## Request-freeness is invariant under lifting

Literal shared constants are unaffected by canonical lifting.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.RequestFree.lift_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#lift-iff).

## Request-freeness is invariant under binder swapping

Canonical binder swap does not turn a nonshared output into a shared one.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.RequestFree.swap_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-05/index.html#swap-iff).

## Request-freeness is invariant under structural congruence

All canonical structural laws preserve absence of an exposed shared request.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.RequestFree.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#cong-iff).

## Service templates are request-free

Existing guarded templates have no exposed output/request.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.ServiceTemplate.request_free`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#request-free).

## Lifting preserves guarded frontiers

Canonical lifting maps guards and existing idle templates literally.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#lift).

## Lifting preserves guarded normal forms

Lifting preserves the actual unguarded private restriction tower.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedNormal.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#lift-2).

## Parallel composition preserves guarded normal forms up to congruence

All private restrictions on either component are extruded canonically;
no process execution or ready pair is stored in the normal form.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedNormal.parallel`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#parallel).

## Runtime-typed processes are congruent to a guarded normal form

ALL10 runtime rules derive a syntactic normal form internally. Replicas
remain actual guarded templates; no recursive process is erased to finite typing.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.syntax_normal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#syntax-normal).

## Guarded normal form of a typed process keeps its typing

Actual runtime normalization retains SAME Γ/n/Δ through the proved Cong
invariance; this theorem supplies the frontier, never the GLOBAL caller.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.frontier_normal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeNormalization.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#frontier-normal).

## Request-free runtime outputs have an active linear subject

A request-free output has an ACTUAL active linear subject and GuardMin.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.linear_out_active`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#linear-out-active).

## Runtime inputs are active linear or have completed ownership

Linear inputs expose active subjects; once-only shared accepts have only
completed AMBIENT ownership and may wait quiescently.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.inp_active_or_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#inp-active-or-completed).

## Request-free completed runtime frontiers are service templates

With no actual requests or active owned keys, typing derives ACTUAL idle
service-template syntax, not merely an empty/completed interface.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.completed_idle`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#completed-idle).

## Minimum active key is the subject of a runtime frontier leaf

A minimum over ALL actual active owned keys exposes the EXACT linear subject
of a real runtime leaf. Idle templates/accept ambient are completed; shared outputs
are excluded only by the internally established request-free case.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.expose_minimum`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#expose-minimum).

## Runtime minimum guard leaf cannot own an equivalent dual peer

The equal-rank semantic peer of a minimum active role cannot share its
actual guard leaf. Opposite roles on the SAME physical name are distinct keys.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.minimum_peer_separate`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontier.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#minimum-peer-separate).

## Non-request-free frontier exposes a shared output up to congruence

A non-request-free frontier yields an ACTUAL declared output leaf through
canonical par rearrangement. Neither readiness nor a progress result is supplied.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.expose_request`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRequests.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRequests.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#expose-request).

## Exposed shared requests step when declared services are available

Any actual exposed request fires under the EXISTING all-declared-services
availability qualifier, even with ZERO active owned keys or a DONE payload.
The Step is constructed from actual offered input syntax, not stored in Available.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.request_progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRequests.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeRequests.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#request-progress).

## Shared invocation and input worker preserve the combined interface

A declared shared invocation and ANY typed input worker preserve their EXACT
combined linear interface. The actual owned payload is substituted, not the
advertised raw protocol; completed receiver annotations remain ambient.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.shared_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSharedHead.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeSharedHead.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#shared-head).

## Inversion of runtime input on a nonshared subject

A nonshared input subject exposes a genuine linear passive or endpoint head.
The shared accept alternative is excluded by actual subject nonalias.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.linear_input_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#linear-input-inv).

## Semantic advance preserves shared-linear separation

Faithful semantic advancement preserves shared/linear separation by its
actual owned-domain invariance, including every completed entry.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.Separated.advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#advance).

## Passive head communication preserves runtime typing

At an INITIALLY compatible disjoint interface, a linear passive head retains
both actual carrier codes and every runtime continuation guard at unchanged Γ.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.passive_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#passive-head-preservation).

## Endpoint head communication preserves runtime typing

At an INITIALLY compatible split, linear endpoint communication transfers
ACTUAL v and keeps the receiver's independent advertised payload/tail codes.
The Γ-preserving runtime substitution retains all continuation priorities.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.endpoint_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#endpoint-head-preservation).

## Runtime head communication advances or keeps the interface

At an INITIALLY semantically compatible linear interface, actual runtime
heads either advance the paired linear subjects faithfully or transfer on a shared
service with the EXACT unchanged interface. Mixed shared/linear heads are excluded
by source separation, not a finite-fragment erasure or supplied result field.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.head_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeCommunication.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-06/index.html#head-advance).

## Same-name linear guards at a compatible interface communicate

Actual disjoint same-name linear leaves at an INITIALLY compatible interface
have opposite directions and construct a canonical Step. Shapes/nonalias are
internally exposed outputs in the GLOBAL proof, not caller readiness hypotheses.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.same_name_linear_guards_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeLinearProgress.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeLinearProgress.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#same-name-linear-guards-step).

## Balanced runtime frontiers are idle or step given availability

A typed balanced runtime frontier with actual persistent service availability
is syntactically Idle OR takes an ACTUAL canonical Step. Shared requests are
handled even if all owned keys are done; minimum/peer leaves are derived internally.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.GuardedFrontier.progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontierProgress.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeFrontierProgress.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#progress).

## Choice selection is the identity on runtime-typed processes

Canonical choice selection is identity on an actually runtime-typed root:
there is no sum rule, although replication is admitted. No finiteLinear erasure.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.select_eq`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#select-eq).

## Subject reduction for runtime typing at compatible interfaces

From a runtime-typed source at an INITIALLY semantically compatible linear
interface, ALL5 canonical Step constructors preserve Γ/n, typing and compatibility.
The actual residual interface is unchanged OR has one faithful SemanticAdvance.
Shared transfers are exact identity; private projection uses the chosen literal pair.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subject_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#subject-reduction).

## Subject reduction for runtime typing at balanced interfaces

An INITIALLY semantically balanced runtime interface derives compatibility
and retains balance and the exact zero-or-one external advance after ANY Step.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subject_reduction_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#subject-reduction-balanced).

## Subject reduction for runtime typing at the empty interface

An empty linear interface is initially balanced/compatible and remains EXACTLY
empty through any runtime Step, including private sessions and shared services.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.subject_reduction_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#subject-reduction-empty).

## Multi-step subject reduction at compatible interfaces

From an INITIALLY compatible runtime interface, finite actual reductions
retain typing/compatibility and accumulate a trace of faithful semantic advances.
Shared/private identity steps introduce no fake external advancement.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.reachable`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#reachable).

## Multi-step subject reduction at balanced interfaces

Every finite reachable state from an INITIALLY balanced runtime interface
retains semantic balance and an ACTUAL faithful advancement trace, not progress.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.reachable_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#reachable-balanced).

## Multi-step subject reduction at the empty interface

Finite runtime execution from an empty interface preserves exact empty
ownership. This safety result does not identify idle replicas with Cong nil.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.reachable_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeReduction.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#reachable-empty).

## Global runtime progress at balanced interfaces given availability

GLOBAL progress at arbitrary ambient n/shared Γ/actual balanced Δ/process p,
qualified ONLY by runtime typing, INITIAL semantic balance and EXISTING persistent
availability of ALL declared signatures. Result is actual Idle syntax OR a canonical
Step. No frontier/normal form/readiness/Step/fairness/representative is supplied.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.progress_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#progress-balanced).

## Closed runtime processes are idle or step given availability

Closed empty-interface runtime progress, at arbitrary passive-name depth,
requires the SAME actual all-declared-service availability. Idle includes waiting
replicas/accepts and nil; no termination or scheduler fairness is asserted.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.progress_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#progress-empty).

## Qualified progress at every reachable runtime state

Every finite canonical reduction from an initially balanced, available typed
runtime retains qualified GLOBAL progress. Safety supplies actual balanced residual
ownership/advance trace, and Available.reachable supplies current persistent syntax.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.reachable_progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#reachable-progress).

## Qualified progress at reachable closed runtime states

Finite reachable empty-interface states retain the same qualified progress;
this is one-step safety/progress, not all-schedules eventual responsiveness.

Formalized by `Cslib.SessionTypes.Endpoint.Runtime.HasType.reachable_progress_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/RuntimeGlobalProgress.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/part-07/index.html#reachable-progress-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Session typing with shared services](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/session-typing-with-shared-services)
