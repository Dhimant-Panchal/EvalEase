export interface Evaluation {
    id: number;
    urn: number;
    marker: number;
    mark?: number;
    module: string;
    assignment_title: string;
}

export interface AcademicProfile {
    id: number;
    full_name: string;
    interests: string[];
}

export interface AcademicReccomendation {
    overlap: number,
    academic: AcademicProfile,
}

export interface SubmissionDetails {
    id: number,
    assignment: number;
    created_at: string;
    keywords: string[];
    marker_count: number;
    urn: number;
}

export interface AssignmentReport {
    all_std_dev: number,
    all_mean: number,
    outliers: {
        score: number,
        submission: SubmissionDetails
    }[],
}