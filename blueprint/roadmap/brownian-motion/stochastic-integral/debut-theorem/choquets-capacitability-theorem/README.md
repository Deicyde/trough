# Choquet's capacitability theorem

This section is devoted to the proof of Choquet's capacitability theorem, which is a key ingredient in the proof of the debut theorem. The presentation follows (bichteler2002stochastic) for the definition of analytic sets (that definition changes a lot between sources) and for the general proof steps, and (he2019semimartingale) and the PlanetMath website for many of the proofs of individual lemmas. Although the definition of analytic sets in (he2019semimartingale) is different, the proofs follow the same general steps and the same ideas, and that book is much more detailed than (bichteler2002stochastic).

## Pavings and Compact systems

A paving is simply a set of sets.

## [supClosure to IsPavingAnalytic.exists_mem_coun…](part-01/README.md)

- [supClosure](part-01/def-supclosure.md)
- [infClosure](part-01/def-infclosure.md)
- [countableSupClosure](part-01/def-countablesupclosure.md)
- [countableInfClosure](part-01/def-countableinfclosure.md)
- [InfClosed.mem_countableInfClosure_iff](part-01/lem-infclosed-mem-countableinfclosure-iff.md)
- [SupClosed.mem_countableSupClosure_iff](part-01/lem-supclosed-mem-countablesupclosure-iff.md)
- [IsCompactSystem](part-01/def-iscompactsystem.md)
- [isCompactSystem_isCompact_isClosed](part-01/lem-iscompactsystem-iscompact-isclosed.md)
- [isCompactSystem_isCompact](part-01/lem-iscompactsystem-iscompact.md)
- [IsCompactSystem.mono](part-01/lem-iscompactsystem-mono.md)
- [isCompactSystem_Icc](part-01/lem-iscompactsystem-icc.md)
- [IsCompactSystem.sigma](part-01/lem-iscompactsystem-sigma.md)
- [IsCompactSystem.prod](part-01/lem-iscompactsystem-prod.md)
- [IsCompactSystem.supClosure](part-01/lem-iscompactsystem-supclosure.md)
- [IsCompactSystem.infClosure](part-01/lem-iscompactsystem-infclosure.md)
- [fst_iInter_of_supClosure_image2_prod_of_antitone](part-01/thm-fst-iinter-of-supclosure-image2-prod-of-anti.md)
- [Analytic set](part-01/def-ispavinganalytic.md)
- [isPavingAnalytic_of_prop](part-01/lem-ispavinganalytic-of-prop.md)
- [IsPavingAnalytic.mono](part-01/lem-ispavinganalytic-mono.md)
- [IsPavingAnalytic.exists_mem_countableSupClosure_superset](part-01/lem-ispavinganalytic-exists-mem-countablesupclos.md)

## [IsPavingAnalytic.iUnion to isCapacitable_of_prop](part-02/README.md)

- [IsPavingAnalytic.iUnion](part-02/lem-ispavinganalytic-iunion.md)
- [IsPavingAnalytic.iInter](part-02/lem-ispavinganalytic-iinter.md)
- [IsPavingAnalytic.fst](part-02/lem-ispavinganalytic-fst.md)
- [IsPavingAnalytic.prod_left](part-02/lem-ispavinganalytic-prod-left.md)
- [IsPavingAnalytic.prod](part-02/lem-ispavinganalytic-prod.md)
- [isPavingAnalytic_isPavingAnalytic](part-02/lem-ispavinganalytic-ispavinganalytic.md)
- [isPavingAnalytic_of_measurableSet_generateFrom](part-02/lem-ispavinganalytic-of-measurableset-generatefr.md)
- [MeasurableSet.isPavingAnalytic_Icc](part-02/lem-measurableset-ispavinganalytic-icc.md)
- [isPavingAnalytic_measurableSet_iff_isPavingAnalytic_Icc](part-02/lem-ispavinganalytic-measurableset-iff-ispavinga.md)
- [MeasurableSet.isPavingAnalytic_image2_prod](part-02/lem-measurableset-ispavinganalytic-image2-prod.md)
- [isPavingAnalytic_fst_of_image2_prod_measurableSet_Icc](part-02/lem-ispavinganalytic-fst-of-image2-prod-measurab.md)
- [MeasurableSet.isPavingAnalytic_fst](part-02/lem-measurableset-ispavinganalytic-fst.md)
- [IsMeasurableAnalytic](part-02/def-ismeasurableanalytic.md)
- [IsMeasurableAnalyticFor.isMeasurableAnalytic](part-02/lem-ismeasurableanalyticfor-ismeasurableanalytic.md)
- [IsMeasurableAnalytic.isPavingAnalytic](part-02/lem-ismeasurableanalytic-ispavinganalytic.md)
- [Capacity](part-02/def-capacity.md)
- [Capacity.compFst_aux](part-02/lem-capacity-compfst-aux.md)
- [Capacity.compFst](part-02/def-capacity-compfst.md)
- [IsCapacitable](part-02/def-iscapacitable.md)
- [isCapacitable_of_prop](part-02/lem-iscapacitable-of-prop.md)

## [isCapacitable_of_mem_countableIn… to Measurable projection](part-03/README.md)

- [isCapacitable_of_mem_countableInfClosure_countableSupClosure](part-03/lem-iscapacitable-of-mem-countableinfclosure-cou.md)
- [fst_image_mem_countableInfClosure](part-03/lem-fst-image-mem-countableinfclosure.md)
- [IsCapacitable.fst](part-03/lem-iscapacitable-fst.md)
- [Choquet's capacitability theorem](part-03/thm-ispavinganalytic-iscapacitable.md)
- [Measure.capacity](part-03/def-measure-capacity.md)
- [Measure.isCapacitable_capacity_iff](part-03/lem-measure-iscapacitable-capacity-iff.md)
- [IsPavingAnalytic.nullMeasurableSet](part-03/lem-ispavinganalytic-nullmeasurableset.md)
- [IsMeasurableAnalytic.nullMeasurableSet](part-03/lem-ismeasurableanalytic-nullmeasurableset.md)
- [Measurable projection](part-03/thm-measurableset-nullmeasurableset-fst.md)
