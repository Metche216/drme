"""
Centralized data store for procedure-specific landing pages.
Each entry defines all content for a dedicated SEO landing page.
Add new procedures here — no other files need to be touched for content.
"""
from urllib.parse import quote

PROCEDURES = {
    "cirugia-tabique-desviado": {
        "slug": "cirugia-tabique-desviado",
        "h1_title": "Corrección de Desvío de Tabique",
        "page_title": "Cirugía de Tabique Desviado en Santa Cruz | Dr. Etcheverry",
        "meta_description": "¿Respirás mal por la nariz? El desvío de tabique tiene solución. Cirugía sin taponaje, recuperación en 2 semanas. Consultorio Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "Mejorar tu calidad de vida es posible y solo toma dos semanas.",
        "pricing_note": "Da el primer paso a tu nueva calidad de vida — solicitá un turno.",
        "whatsapp_message": "Hola! Me gustaría consultar sobre la cirugía de tabique.",
        "cta_headline": "¿Listo/a para mejorar tu calidad de vida?",
        "hero_image": "images/septum/septum .jpg",
        "hero_image_alt": "Anatomía del tabique nasal",
        "treatment_image": "images/septum/septum incision.jpg",
        "treatment_image_alt": "Técnica quirúrgica de septoplastia",
        "symptoms": [
            "Obstrucción nasal permanente",
            "Dificultad para respirar por la nariz durante la actividad física",
            "Dificultad para conciliar el sueño",
            "Tendencia a sinusitis recurrente",
            "Dolores de cabeza frecuentes",
            "Respiración ruidosa o con esfuerzo",
        ],
        "treatment_html": """
            <p>La técnica quirúrgica se fue modernizando a lo largo de los años. Hoy en día
            se realiza completamente por el orificio nasal, <strong>sin dejar hematomas ni
            cicatrices visibles</strong>. Se realiza una pequeña incisión dentro de la nariz
            y se trabaja el desvío del cartílago y del hueso a través de la misma.</p>
            <p>Al final de la cirugía se realizan suturas internas que nos permiten
            <strong>evitar el uso de taponajes incómodos y dolorosos</strong>. En algunos
            casos utilizamos férulas de silicona que permiten el pasaje del aire durante
            toda la recuperación.</p>
        """,
        "recovery_html": """
            <p>Luego de la cirugía se realizan <strong>1 o 2 controles semanales</strong>
            para limpieza de costras y secreciones. La frecuencia dependerá de la capacidad
            de cicatrización de cada paciente.</p>
            <ul>
                <li>En condiciones normales, a los <strong>7–10 días</strong> se pueden retomar
                actividades laborales que no impliquen esfuerzo físico.</li>
                <li>A los <strong>15–20 días</strong> se puede retomar actividad física con
                normalidad.</li>
            </ul>
        """,
        "faq_items": [
            {
                "question": "¿La cirugía de tabique va a cambiar el aspecto de mi nariz?",
                "answer": "No. Esta cirugía es de carácter estrictamente funcional y no tiene ningún impacto estético. El objetivo es optimizar el flujo de aire a través de la nariz, sin modificar su forma externa ni dejar cicatrices visibles.",
            },
            {
                "question": "¿Qué tipo de anestesia se usa? ¿Voy a estar dormido?",
                "answer": "Sí, el paciente está dormido durante el procedimiento ya que se realiza bajo anestesia general. El equipo de anestesiología estará presente durante toda la intervención para garantizar tu seguridad y confort.",
            },
            {
                "question": "¿Es una cirugía dolorosa? ¿Qué voy a sentir después?",
                "answer": "Como en todo procedimiento invasivo, es esperable algo de dolor, pero no es la queja principal de los pacientes postoperados. Lo más frecuente es la sensación de congestión nasal, similar a un resfrío fuerte, que va cediendo progresivamente durante la recuperación.",
            },
            {
                "question": "¿Cuándo voy a poder respirar bien después de la cirugía?",
                "answer": "El resultado es inmediato: al despertar de la anestesia ya notarás la diferencia. Sin embargo, hay un proceso de recuperación de aproximadamente dos semanas durante el cual es normal sentir la nariz algo tapada debido a la inflamación interna.",
            },
            {
                "question": "¿Existe riesgo de que el desvío vuelva a aparecer o que la cirugía no funcione?",
                "answer": "El riesgo es muy bajo, pero existe. La gran mayoría de las complicaciones pueden atenderse a tiempo si el paciente concurre a sus controles postoperatorios programados. Por eso el seguimiento regular es parte fundamental del tratamiento.",
            },
            {
                "question": "¿Qué cuidados tengo que tener en casa después de la operación?",
                "answer": "Principalmente evitar exposición a altas temperaturas (sol intenso, baños muy calientes) y esfuerzos físicos durante las primeras dos semanas, para prevenir el sangrado postoperatorio. También es importante no sonarse la nariz con fuerza y seguir las indicaciones de higiene nasal que se indican en el postoperatorio.",
            },
        ],
    },

    "apnea-del-sueno-ronquidos": {
        "slug": "apnea-del-sueno-ronquidos",
        "h1_title": "Cirugía para Ronquidos y Apnea del Sueño",
        "page_title": "Tratamiento de Apnea del Sueño y Ronquidos en Santa Cruz | Dr. Etcheverry",
        "meta_description": "Roncás fuerte o te despertás cansado? La apnea del sueño tiene tratamiento. Evaluación especializada y cirugía multinivel. Consultorio Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "Mejorá tu salud y tu capacidad de descansar.",
        "pricing_note": "Consulta de valoración y estudio del sueño",
        "whatsapp_message": "Hola! Me gustaría consultar sobre el tratamiento de ronquidos y apnea del sueño.",
        "cta_headline": "¿Tu sueño puede mejorar?",
        "hero_image": "images/Ronquidos/apnea_hero.jpg",
        "hero_image_alt": "Apnea del sueño - vía aérea superior",
        "treatment_image": "images/Ronquidos/CENS.jpg",
        "treatment_image_alt": "Tratamiento quirúrgico de vía aérea",
        "symptoms": [
            "Ronquido nocturno intenso",
            "Cefalea al despertar por las mañanas",
            "Somnolencia excesiva durante el día",
            "Pausas respiratorias durante el sueño",
            "Cambios en la atención y el estado de ánimo",
            "Sensación de ahogo o despertar brusco durante la noche",
        ],
        "treatment_html": """
            <p>Existe un proceso diagnóstico que permite identificar el grado de severidad
            de la enfermedad y sus posibles causas. Algunas requieren <strong>tratamiento
            quirúrgico</strong>, otras farmacológico o mediante dispositivos de asistencia
            como el CPAP. En muchos casos el abordaje es <strong>multidisciplinario</strong>
            y requiere valoración por distintas especialidades.</p>
            <p>Cuando la alternativa es quirúrgica, se utilizan <strong>técnicas de cirugía
            multinivel</strong>, adaptadas al sitio específico de obstrucción de cada
            paciente. El objetivo es generar cambios definitivos en la anatomía de la vía
            respiratoria superior para restablecer un flujo de aire adecuado durante el
            sueño.</p>
        """,
        "recovery_html": """
            <p>El postoperatorio dependerá del sitio principal de trabajo quirúrgico:</p>
            <ul>
                <li>Si la cirugía involucra la <strong>orofaringe</strong> (paladar blando,
                amígdalas, base de lengua), es esperable mayor dolor postoperatorio. El
                período de convalecencia varía entre <strong>2 y 3 semanas</strong>.</li>
                <li>Si el sitio principal de trabajo es la <strong>fosa nasal</strong>,
                la molestia principal es la congestión nasal, habitualmente mejor tolerada.</li>
            </ul>
            <p>En todos los casos se realizan controles postoperatorios para acompañar
            la evolución y ajustar el tratamiento si fuera necesario.</p>
        """,
        "faq_items": [
            {
                "question": "¿Cómo sé si tengo apnea del sueño o solo ronco?",
                "answer": "Eso se define fácilmente mediante un estudio de Polisomnografía en internación, o una Poligrafía Respiratoria Domiciliaria, según cuál corresponda a tu caso. En la consulta determinamos qué estudio es el más adecuado para vos.",
            },
            {
                "question": "¿La cirugía cura definitivamente la apnea del sueño?",
                "answer": "No siempre de forma total, y por eso es fundamental una evaluación rigurosa que identifique todos los componentes de la enfermedad. La cirugía resuelve los problemas estructurales de la anatomía de la vía respiratoria superior, que es uno de los factores clave.",
            },
            {
                "question": "¿Qué diferencia hay entre usar CPAP y operarse?",
                "answer": "Son alternativas distintas. El CPAP es un tratamiento paliativo: revierte las apneas mientras se utiliza cada noche, pero no modifica la causa. La cirugía, en cambio, genera cambios definitivos en la anatomía de la vía aérea.",
            },
            {
                "question": "¿Es necesario hacer un estudio del sueño antes de la cirugía?",
                "answer": "Sí. La Polisomnografía es el estudio de elección para el diagnóstico de las apneas y es muy importante realizarla previamente a cualquier decisión quirúrgica. Nos permite medir la severidad real de la enfermedad y planificar el tratamiento adecuado.",
            },
            {
                "question": "¿Es dolorosa la cirugía de ronquidos? ¿Cuánto tiempo de recuperación tiene?",
                "answer": "El trabajo sobre la musculatura faríngea suele ser más incómodo que el trabajo en otras áreas de la vía respiratoria. El período de convalecencia varía entre 2 y 3 semanas dependiendo de las técnicas utilizadas.",
            },
            {
                "question": "¿Hay restricciones por edad o condición física para operarse?",
                "answer": "La edad en sí no es un problema. Lo más importante es contar con un buen diagnóstico. Las restricciones dependen de las enfermedades de base del paciente, especialmente su estado metabólico: peso, presión arterial, hábitos y estado psicoemocional.",
            },
        ],
    },

    "amigdalectomia": {
        "slug": "amigdalectomia",
        "h1_title": "Amigdalectomía — Sin Cortes, Sin Puntos",
        "page_title": "Cirugía de Amígdalas en Santa Cruz | Amigdalectomía Dr. Etcheverry",
        "meta_description": "¿Anginas a repetición? La amigdalectomía es una solución definitiva. Técnica capsular sin cortes externos, procedimiento ambulatorio. Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "Dejá atrás las anginas a repetición. Para siempre.",
        "pricing_note": "Procedimiento ambulatorio · Alta el mismo día",
        "whatsapp_message": "Hola! Me gustaría consultar sobre la operación de amígdalas.",
        "cta_headline": "¿Ya es momento de encontrar una solución definitiva?",
        "hero_image": "images/amigdalas/IMG_5072.JPG",
        "hero_image_alt": "Amígdalas - cirugía de garganta",
        "treatment_image": "images/amigdalas/490892015_2370760163300668_5060922596504098637_n.jpg",
        "treatment_image_alt": "Amigdalectomía - técnica capsular",
        "symptoms": [
            "Obstrucción respiratoria en la infancia",
            "Infecciones de garganta a repetición (anginas frecuentes)",
            "Cálculos amigdalinos (tonsilolitos)",
            "Antecedentes de abscesos faríngeos",
            "Dificultad para tragar en la infancia",
            "Ronquidos o apnea asociada a hipertrofia amigdalina",
        ],
        "treatment_html": """
            <p>Cuando se cumplen los criterios necesarios, la indicación es quirúrgica.
            La amigdalectomía se realiza <strong>a través de la cavidad oral</strong>,
            sin necesidad de hacer cortes externos ni suturas en la piel.</p>
            <p>Se utilizan <strong>técnicas capsulares</strong> que permiten remover la
            totalidad de la amígdala, garantizando que no queden residuos que puedan
            provocar nuevas infecciones. El procedimiento es <strong>ambulatorio</strong>:
            el paciente ingresa y se retira el mismo día, realizando la recuperación
            en el domicilio.</p>
        """,
        "recovery_html": """
            <p>En <strong>niños</strong> la recuperación es más rápida. En <strong>adultos</strong>
            toma un poco más de tiempo debido al mayor trabajo muscular y la memoria
            del tejido de cada grupo etario.</p>
            <ul>
                <li>Es una cirugía que genera <strong>dolor postoperatorio</strong>, pero este
                puede manejarse muy bien con terapia analgésica de primer nivel.</li>
                <li>Se requieren <strong>restricciones alimenticias básicas</strong> durante
                los primeros días (dieta blanda y fría).</li>
                <li>El período de convalecencia es de aproximadamente
                <strong>15 a 20 días</strong>.</li>
            </ul>
        """,
        "faq_items": [
            {
                "question": "¿A qué edad se puede operar de las amígdalas?",
                "answer": "Si bien no existe un límite de edad cuando la indicación es primaria, intentamos indicar la cirugía a partir de que los planes de vacunación están completos, es decir, desde los 2 años en adelante.",
            },
            {
                "question": "¿Es una cirugía con mucho dolor postoperatorio?",
                "answer": "Es una cirugía que genera dolor, sí. Sin embargo, existen terapias analgésicas de primer nivel que permiten reducir esa incomodidad al mínimo. La clave es seguir el esquema de medicación indicado y no esperar a que el dolor aparezca para tomarlo.",
            },
            {
                "question": "¿Cuándo está indicada la amigdalectomía? ¿No alcanza con antibióticos?",
                "answer": "Los antibióticos resuelven el episodio puntual, pero no la recurrencia. Cuando una persona tiene 4 o más episodios de amigdalitis bacteriana al año, recomendamos la extirpación definitiva como la solución más eficaz.",
            },
            {
                "question": "¿Cuánto tiempo tarda la recuperación para volver al trabajo?",
                "answer": "Entre 2 y 3 semanas, dependiendo del tipo de actividad laboral. Trabajos de oficina pueden retomarse antes; actividades que impliquen hablar mucho o esfuerzo físico requieren un poco más de tiempo.",
            },
            {
                "question": "¿La operación afecta las defensas del organismo?",
                "answer": "En absoluto. Las amígdalas son una de las tantas herramientas del sistema inmunológico, pero no son indispensables para su funcionamiento normal. Extirparlas no genera inmunodeficiencia.",
            },
            {
                "question": "¿Hay riesgo de hemorragia después de la operación?",
                "answer": "Sí, es la complicación más temida. Para minimizar ese riesgo trabajamos con mucha atención en quirófano y damos indicaciones muy claras sobre las medidas de prevención durante el alta: reposo, dieta adecuada y evitar esfuerzos.",
            },
        ],
    },

    "cirugia-de-oido": {
        "slug": "cirugia-de-oido",
        "h1_title": "Cirugía de Oído — Microscópica y Endoscópica",
        "page_title": "Cirugía de Oído en Santa Cruz de la Sierra | Dr. Etcheverry",
        "meta_description": "Perforación timpánica, colesteatoma, hipoacusia. Cirugía de oído microscópica y endoscópica en Santa Cruz. Diagnóstico y resolución en consulta. +59175174664.",
        "hero_subtitle": "Tecnología de primer nivel para restaurar tu audición y la salud de tu oído.",
        "pricing_note": "Consulta de valoración con endoscopía de alta definición",
        "whatsapp_message": "Hola! Me gustaría consultar sobre una cirugía de oído.",
        "cta_headline": "¿Tu oído merece atención especializada?",
        "hero_image": "images/Oido/494216822_2384174458625905_7175777455310681778_n.jpg",
        "hero_image_alt": "Cirugía de oído con microscopio quirúrgico",
        "treatment_image": "images/Oido/IMG_1003.JPG",
        "treatment_image_alt": "Procedimiento de timpanoplastia",
        "symptoms": [
            "Perforación timpánica",
            "Secreción constante del oído",
            "Pérdida auditiva asociada a daño timpánico",
            "Cirugía previa de oído",
            "Colesteatoma de oído medio",
            "Otoesclerosis",
        ],
        "treatment_html": """
            <p>La cirugía de oído abarca un amplio espectro de patologías, y el tratamiento se planifica de forma personalizada según el diagnóstico:</p>
            <ul>
                <li><strong>Timpanoplastia:</strong> Cierre de perforaciones de la membrana timpánica con o sin reconstrucción osicular (usando autoinjertos de fascia o cartílago).</li>
                <li><strong>Cirugía de colesteatoma y otitis media crónica:</strong> Resección de pseudotumores del oído medio, mastoides y bolsas de retracción.</li>
                <li><strong>Reconstrucción osicular:</strong> Con autoinjertos o prótesis para restaurar la transmisión del sonido.</li>
                <li><strong>Cirugía estapedial:</strong> Reemplazo del estribo por enfermedades genéticas que llevan a la fijación.</li>
            </ul>
            <p>Todo realizado con <strong>microscopio quirúrgico o endoscopía de alta definición</strong>.</p>
        """,
        "recovery_html": """
            <p>La recuperación varía según la técnica y el diagnóstico.</p>
            <p>La fase de convalecencia inicial dura aproximadamente entre tres y siete días, en donde el oído estará cubierto. Luego sigue una fase de recuperación que es de aproximadamente dos a tres semanas en donde es necesario cuidar el oído del agua.</p>
            <p>Finalmente, enfermedades más complejas requieren tiempos de recuperación más largos (a veces meses).</p>
        """,
        "faq_items": [
            {
                "question": "¿Una perforación timpánica se puede curar sin cirugía?",
                "answer": "Sí, en general cuando son de origen traumático y si se hacen los cuidados apropiados. Pero las perforaciones por infección o de larga data, no suelen cerrar espontáneamente.",
            },
            {
                "question": "¿La cirugía de oído mejora la audición?",
                "answer": "El beneficio auditivo no es objetivo de la operación, en general mejora pero no podemos prometerle al paciente que eso va a ocurrir.",
            },
            {
                "question": "¿Cuánto dura la recuperación?",
                "answer": "En términos generales, entre 3 y 4 semanas, pero depende de cada patología y el tipo de cirugía.",
            },
            {
                "question": "¿Se puede operar con otitis activa o hay que esperar?",
                "answer": "Lo mejor es esperar entre 2 y 3 meses hasta que el oído esté seco, sin infección activa.",
            },
            {
                "question": "¿Qué es el colesteatoma y es peligroso?",
                "answer": "El colesteatoma es una enfermedad crónica del oído que ocurre por la retracción del tímpano hacia adentro del oído y el atrapamiento de piel descamada. Se comporta de una forma muy parecida a un tumor, desgastando las estructuras del oído interno, pero no es un tumor ni un cáncer. Tampoco maligniza, ni metastatiza.",
            },
            {
                "question": "¿La cirugía de oído se hace con anestesia general?",
                "answer": "Sí, es necesario que el paciente esté completamente inmóvil para poder trabajar con tranquilidad.",
            },
        ],
    },

    "cirugia-sinusal-cens": {
        "slug": "cirugia-sinusal-cens",
        "h1_title": "Cirugía Sinusal Endoscópica (CENS)",
        "page_title": "Cirugía Sinusal Endoscópica CENS en Santa Cruz | Dr. Etcheverry",
        "meta_description": "Sinusitis crónica o poliposis nasal con solución definitiva. CENS sin incisiones, ambulatoria y de recuperación rápida. Consultorio Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "Mínimamente invasiva. Sin cicatrices. Recuperación en dos semanas.",
        "pricing_note": "Procedimiento ambulatorio · Sin incisiones externas",
        "whatsapp_message": "Hola! Me gustaría consultar sobre la cirugía sinusal o poliposis nasal.",
        "cta_headline": "¿Tu nariz puede respirar mejor?",
        "hero_image": "images/CENS/490679252_2366962333680451_2833912752244573939_n.jpg",
        "hero_image_alt": "Cirugía sinusal endoscópica CENS",
        "treatment_image": "images/CENS/494150422_2383583215351696_2540311705557602608_n.jpg",
        "treatment_image_alt": "Endoscopio rígido para cirugía nasal",
        "symptoms": [
            "Congestión nasal crónica que no cede con medicación",
            "Sinusitis recurrente o crónica",
            "Poliposis nasal",
            "Secreción nasal posterior (goteo retronasal)",
            "Cefalea y presión facial de origen sinusal",
            "Hemorragias nasales severas",
        ],
        "treatment_html": """
            <p>La CENS es una cirugía endoscópica que se realiza <strong>a través de
            los orificios naturales de la nariz</strong>, sin ningún tipo de incisión
            externa ni cicatriz visible. Con cámaras y pinzas de alta precisión se abren
            y drenan los senos afectados, y se extirpan los pólipos cuando están
            presentes.</p>
            <p>El procedimiento es <strong>ambulatorio</strong>: el paciente ingresa y
            se retira el mismo día, realizando la recuperación en el domicilio. En algunos
            casos se combina con la corrección del tabique o
            <strong>turbinoplastia</strong> para optimizar el resultado funcional.</p>
        """,
        "recovery_html": """
            <p>La congestión y el sangrado leve son esperables en los primeros días.
            Se realizan <strong>controles postoperatorios semanales</strong> para limpiar
            la cavidad y evaluar la evolución:</p>
            <ul>
                <li>A los <strong>7–10 días</strong> se pueden retomar actividades
                laborales de bajo esfuerzo.</li>
                <li>La actividad física plena se retoma a los
                <strong>15–20 días</strong>.</li>
            </ul>
        """,
        "faq_items": [
            {
                "question": "¿La CENS deja cicatrices?",
                "answer": "No. Todo el abordaje es a través de los orificios naturales de la nariz. No hay cortes en la piel ni cicatrices visibles.",
            },
            {
                "question": "¿Los pólipos vuelven a aparecer después de operarse?",
                "answer": "Existe esa posibilidad, especialmente en pacientes con alergia de base. El tratamiento médico postoperatorio (corticoides nasales, lavados) es clave para reducir la recurrencia y prolongar los resultados de la cirugía.",
            },
            {
                "question": "¿Es necesario usar taponajes después de la cirugía?",
                "answer": "No de forma rutinaria. En la mayoría de los casos se evitan los taponajes incómodos gracias a las técnicas actuales y al uso de suturas o materiales reabsorbibles.",
            },
            {
                "question": "¿Cuánto tiempo tarda en volver el olfato?",
                "answer": "Varía según cada caso. En muchos pacientes mejora progresivamente durante las primeras semanas postoperatorias; en casos de poliposis severa o larga data, la recuperación del olfato puede tomar más tiempo.",
            },
            {
                "question": "¿Se puede evitar la cirugía con medicamentos?",
                "answer": "Si la sinusitis es leve o moderada, sí. La cirugía está indicada cuando el tratamiento médico bien conducido — antibióticos, corticoides y lavados nasales — no logra controlar los síntomas de forma sostenida.",
            },
            {
                "question": "¿La cirugía se hace con anestesia general?",
                "answer": "Sí, en la mayoría de los casos. La anestesia general garantiza la comodidad del paciente y la precisión del cirujano en un área anatómica de alta complejidad.",
            },
        ],
    },

    "implante-coclear": {
        "slug": "implante-coclear",
        "h1_title": "Cirugía de Implante Coclear",
        "page_title": "Implante Coclear en Santa Cruz | Dr. Etcheverry",
        "meta_description": "La cirugía más avanzada para recuperar la audición en casos de hipoacusia severa a profunda. Evaluación, cirugía y activación. Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "La tecnología de máxima precisión para recuperar un órgano de los sentidos y volver a conectarte con tu entorno.",
        "pricing_note": "Evaluación audiológica integral y planificación quirúrgica",
        "whatsapp_message": "Hola! Me gustaría consultar sobre la cirugía de implante coclear.",
        "cta_headline": "¿Listo/a para dar el primer paso hacia una mejor audición?",
        "symptoms": [
            "Pérdida auditiva total uni o bilateral",
            "Hipoacusia Súbita",
            "Hipoacusias congénitas",
            "Hipoacusia profunda adquirida",
            "Falta de beneficio con audífonos convencionales",
        ],
        "treatment_html": """
            <p>Es la <strong>cirugía más avanzada en nuestra especialidad</strong>. Consiste en colocar un implante de silicona milimétricamente dentro del oído interno, a través de una incisión detrás de la oreja, para que este pueda estimular directamente al nervio auditivo.</p>
            <p>Representa un procedimiento de máxima precisión y tecnología, siendo el <strong>único que permite recuperar efectivamente un órgano de los sentidos</strong> cuando las células ciliadas están dañadas o ausentes.</p>
        """,
        "recovery_html": """
            <p>Se realizan controles semanales luego de la cirugía hasta cumplir un mes aproximadamente, momento en el cual se realiza la <strong>activación del dispositivo</strong> (el encendido inicial).</p>
            <p>Posterior a su activación, es imprescindible realizar un trabajo sostenido de <strong>adaptación y educación audioverbal</strong> en conjunto con el equipo de fonoaudiología. El cerebro necesita aprender a interpretar los nuevos estímulos sonoros, por lo que el compromiso con la rehabilitación es clave para el éxito del implante.</p>
        """,
        "faq_items": [
            {
                "question": "¿El implante coclear es igual a un audífono?",
                "answer": "No, pero sí necesita un procesador externo que es inclusive un poco más grande que un audífono. Siempre se necesita un micrófono fuera de la piel para que reciba el sonido y lo transmita al procesador interno.",
            },
            {
                "question": "¿La cirugía se realiza con anestesia general y voy a sentir dolor?",
                "answer": "Sí, es bajo anestesia general, ya que es una cirugía delicada. El dolor es fácilmente manejable con analgésicos habituales.",
            },
            {
                "question": "¿Cuándo voy a empezar a escuchar después de la cirugía?",
                "answer": "Al mes, cuando se hace la activación, se escuchan los primeros sonidos. Sin embargo, el proceso se perfecciona con el tiempo.",
            },
            {
                "question": "¿Escucharé 'normal' apenas se encienda el dispositivo?",
                "answer": "No exactamente, es necesaria una reeducación auditiva y con el tiempo se normaliza. Este proceso puede durar meses.",
            },
            {
                "question": "¿Requiere algún cuidado especial a largo plazo?",
                "answer": "El implante como tal requiere calibraciones, cambio de baterías y todos los cuidados lógicos de un dispositivo electrónico. El procesador interno queda debajo de la piel y se comunica con el externo a través de una conexión magnética.",
            },
        ],
    },

    "vertigo-mareos": {
        "slug": "vertigo-mareos",
        "h1_title": "Estudio y Tratamiento del Vértigo",
        "page_title": "Tratamiento de Vértigo y Mareos en Santa Cruz | Dr. Etcheverry",
        "meta_description": "¿Sentís que todo da vueltas o perdés el equilibrio? Evaluación otoneurológica especializada para el tratamiento definitivo del vértigo. Dr. Etcheverry · +59175174664.",
        "hero_subtitle": "Recuperá tu equilibrio y tu seguridad. Un diagnóstico preciso es el primer paso.",
        "pricing_note": "Evaluación otoneurológica y maniobras de reposicionamiento",
        "whatsapp_message": "Hola! Me gustaría consultar por problemas de vértigo, mareos o pérdida de equilibrio.",
        "cta_headline": "¿Listo/a para volver a moverte sin mareos?",
        "symptoms": [
            "Sensación de giro o de que el entorno se mueve (Vértigo)",
            "Inestabilidad o pérdida de equilibrio al caminar",
            "Mareos intensos al cambiar de postura (ej. al acostarse o girar en la cama)",
            "Náuseas, vómitos o sudoración fría acompañando al mareo",
            "Zumbidos en los oídos (acúfenos) o sensación de oído tapado",
            "Sensación de aturdimiento o 'cabeza hueca'",
        ],
        "treatment_html": """
            <p>El abordaje del vértigo y los mareos comienza con una <strong>evaluación otoneurológica exhaustiva</strong> para identificar la causa exacta, ya que el oído interno es el centro principal del equilibrio.</p>
            <p>Dependiendo del diagnóstico (como el Vértigo Posicional Paroxístico Benigno, la Enfermedad de Ménière o una neuritis vestibular), el tratamiento puede incluir <strong>maniobras de reposicionamiento canalicular en consultorio</strong>, terapia farmacológica específica o el diseño de un programa de <strong>rehabilitación vestibular</strong>.</p>
        """,
        "recovery_html": """
            <p>La recuperación depende enteramente de la patología de base. En casos muy frecuentes como el vértigo posicional (VPPB), las maniobras físicas en consultorio pueden <strong>aliviar los síntomas de manera inmediata</strong> o en muy pocos días.</p>
            <p>En cuadros inflamatorios o más complejos, la rehabilitación vestibular guiará al cerebro para compensar el déficit de equilibrio, logrando una mejoría progresiva y sostenida que te permitirá retomar tus actividades habituales sin temor a nuevas crisis.</p>
        """,
        "faq_items": [
            {
                "question": "¿Cuál es la diferencia entre vértigo y mareo?",
                "answer": "El vértigo es una ilusión específica de movimiento (sentir que tú o la habitación giran), y suele estar causado por problemas en el oído interno. El mareo es una sensación más general de inestabilidad, aturdimiento o debilidad que puede deberse a múltiples factores sistémicos.",
            },
            {
                "question": "¿Es grave tener crisis de vértigo?",
                "answer": "La gran mayoría de los cuadros de vértigo son de origen periférico (del oído) y, aunque los síntomas pueden ser sumamente intensos y angustiantes, son tratables y no representan una amenaza grave para la salud. Sin embargo, una evaluación médica es fundamental para confirmar el diagnóstico y descartar otras causas.",
            },
            {
                "question": "¿Las pastillas para el mareo curan el problema?",
                "answer": "No. Los medicamentos antivertiginosos o sedantes vestibulares son útiles para controlar los síntomas agudos (como náuseas y vómitos), pero no curan la causa subyacente. De hecho, si se usan por tiempo prolongado, pueden retrasar la compensación natural del cerebro para recuperar el equilibrio.",
            },
            {
                "question": "¿En qué consisten las maniobras de reposicionamiento?",
                "answer": "Son secuencias de movimientos específicos de la cabeza y el cuerpo que el especialista realiza en el consultorio. Su objetivo es devolver unas pequeñas partículas de calcio (otoconias) que se han salido de lugar en el oído interno hacia su posición correcta, curando el vértigo posicional de forma rápida.",
            },
        ],
    },
}


def get_procedure(slug):
    """Return a procedure dict with computed fields, or None if not found."""
    proc = PROCEDURES.get(slug)
    if not proc:
        return None
    # Compute URL-encoded WhatsApp message on the fly
    result = dict(proc)
    result["whatsapp_encoded_message"] = quote(proc["whatsapp_message"])
    return result
